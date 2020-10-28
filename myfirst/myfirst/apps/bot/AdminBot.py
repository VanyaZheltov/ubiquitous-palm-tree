import time
import random
import vk_api
import vk
from vk_api.longpoll import VkLongPoll, VkEventType
import json
from .MainBot import write_msg
import requests
from . import keyboard
from . import admin_commands
import re

login = {
    'is_logged': False,
    'site': 'None'
}


token_admin = "74e43e6ece7717fcaf61ade275b6a30fdeae86961123e3707d7b81b5e40799128f0be4991924e5898a4ab"
vk_admin = vk_api.VkApi(token=token_admin)

longpoll_admin = VkLongPoll(vk_admin)
api = vk.Api(token_admin)
vka = vk_admin.get_api() 

group = api.get_group('public198013200')  #Получение инфо о группе
user_items = []

def get_username(user_id: int):
    user_get=vka.users.get(user_ids = (user_id))
    user_get=user_get[0]
    first_name=user_get['first_name']
    return first_name

#Механизм отправки сообщений
def write_admin(user_id, message, keyboard=None, attachment=None):
    vk_admin.method('messages.send', {'user_id': user_id, 'message': message,'keyboard': keyboard if keyboard != None else [],"attachment": attachment if attachment != None else None, 'random_id': random.randint(0,11111)})

def start_admin():
    last_event = "none"

    print('Админ Бот запущен')

    for event in longpoll_admin.listen(): #Прослушивание сервера ВК

        if event.type == VkEventType.MESSAGE_NEW: #Если событие == новому сообщению

            if event.to_me: #Если сообщение для бота
                
                
                msg = event.text #Получение сообщения
                print('Admin: ' + str(event.user_id)) #Логгирование сообщения
                
                #Команда для рассылки сообщения(следующее сообщение будет разослано всем кто в группе BotTest)
                if msg.lower() in admin_commands.mailcommands:
                    write_admin(event.user_id, "Введите сообщение для отправки или нажмите на кнопку для отмены:", keyboard.cancelkeyboard)
                    last_event = msg.lower()

                if msg.lower().startswith(admin_commands.special_login):
                    if login['is_logged'] == False:
                        data = msg.split(';')
                        for i in range(0, len(data)):
                            data[i] = data[i].strip()
                        try:                                                
                            if data[1] in admin_commands.users:
                                if data[2] in admin_commands.users[data[1]]['login']:
                                    if data[3] in admin_commands.users[data[1]]['password']:
                                        login['is_logged'] = True
                                        login['site'] = data[1]
                                        write_admin(event.user_id, f"{get_username(event.user_id)}, Вы авторизованы как {data[2]} на сайте {data[1]}!")
                                    else:
                                        write_admin(event.user_id, "Неверный логин или пароль!")
                                else:
                                    write_admin(event.user_id, "Неверный логин или пароль!")
                            else:
                                write_admin(event.user_id, "Неверное название сайта!")
                        except:
                            write_admin(event.user_id, "Ошибка авторизации! Попробуйте снова! (a; сайт; логин; пароль;)")
                    else:
                        write_admin(event.user_id, f"{get_username(event.user_id)}, Вы уже авторизованы! Используйте '{admin_commands.unauthorize_command}' для деавторизации!")
                if msg.lower() == admin_commands.unauthorize_command:
                    login['is_logged'] = False
                    login['site'] = "None"
                    write_admin(event.user_id, f"{get_username(event.user_id)}, вы деавторизованы! Вы можете авторизоваться снова при помощи команды 'a'(a; сайт; логин; пароль;)!")
                
                #Механизм рассылки с отменой
                if last_event == "r" and len(msg) > 1:
                    if msg.lower() not in admin_commands.cancelcommands: 
                        last_event = "msg"
                        user_items = [user for user in group.get_members_only_id()]
                        mail_users = 0 #Пользователи получившие рассылку
                        for user_id in user_items:
                            try:
                                write_msg(user_id, msg)
                                mail_users += 1
                            except:
                                print('Ошибка при отправке сообщения!')
                        write_admin(event.user_id, f"Рассылка совершена! Пользователей получивших рассылку: {mail_users}")
                        mail_users = 0
                    else:
                        write_admin(event.user_id, "Рассылка отменена!")
                        last_event = "none"
                #Защитный механизм
                elif len(msg) == 1 and last_event == "r":
                    write_admin(event.user_id, "Длина сообщения должна быть минимум 2 символа! ('Отмена' для отмены отправки)")

                #Получение количества всех пользователей(id) в группе
                if last_event != "r" and msg.lower() in admin_commands.idcommands:
                    user_items = [user for user in group.get_members_only_id()]
                    write_admin(event.user_id, f"Всего пользователей в группе: {str(len(user_items))}")

                #Вывод всех команд
                if msg.lower() in admin_commands.helpcommands:
                    help_msg = """"""
                    for command in admin_commands.commands:
                        help_msg += f"""\n{command}"""
                        for i in range(0, len(admin_commands.commands[command])):
                            help_msg += f"""\n• {admin_commands.commands[command][i]}"""
                    write_admin(event.user_id, help_msg)
                #Если команда не распознана
                else:
                    pass
                
                """https://oauth.vk.com/authorize?client_id=7611116&display=page&redirect_uri=https://englishpush.online/tables/&scope=photos&response_type=token&state=123456"""

                
                