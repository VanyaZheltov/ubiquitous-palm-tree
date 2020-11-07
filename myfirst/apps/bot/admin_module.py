import vk_api
from .keyboard import *
from .admin_commands import *
from .main_config import *
import vk

last_event = "None"
login = {
    'is_logged': False,
    'site': 'None'
}
vk_admin = vk_api.VkApi(token=admin_token)
vka = vk_admin.get_api()
api = vk.Api(admin_token)
group = api.get_group('public198013200')  #Получение инфо о группе
user_items = []
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()

def write_main(user_id, message, keyboard=None, attachment=None):
    vk_session.method('messages.send', {'user_id': user_id, 'message': message,'keyboard': keyboard if keyboard != None else [],"attachment": attachment if attachment != None else None, 'random_id': random.randint(0,11111)})
    
def write_admin(user_id, message, keyboard=None, attachment=None):
    vk_admin.method('messages.send', {'user_id': user_id, 'message': message,'keyboard': keyboard if keyboard != None else [],"attachment": attachment if attachment != None else None, 'random_id': random.randint(0,11111)})

def mail(admin_id, msg):
    user_items = [user for user in group.get_members_only_id()]
    mail_users = 0 #Пользователи получившие рассылку
    for user_id in user_items:
        try:
            write_msg(user_id, msg)
            mail_users += 1
        except:
            print('Ошибка при отправке сообщения!')
    write_admin(admin_id, f"Рассылка совершена! Пользователей получивших рассылку: {mail_users}")
    mail_users = 0

def get_username(user_id: int):
    user_get=vka.users.get(user_ids = (user_id))
    user_get=user_get[0]
    first_name=user_get['first_name']
    return first_name

def AdminHandler(user_id, msg):
    if msg.lower().startswith(special_login):
        if login['is_logged'] == False:
            data = msg.split(';')
            for i in range(0, len(data)):
                data[i] = data[i].strip()
                try:                                                #Логин
                    if data[1] in users:
                        if data[2] in users[data[1]]['login']:
                            if data[3] in users[data[1]]['password']:
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
            write_admin(event.user_id, f"{get_username(event.user_id)}, Вы уже авторизованы! Используйте '{unauthorize_command}' для деавторизации!")
    if msg.lower() == unauthorize_command:
        login['is_logged'] = False
        login['site'] = "None"
        write_admin(event.user_id, f"{get_username(event.user_id)}, вы деавторизованы! Вы можете авторизоваться снова при помощи команды 'a'(a; сайт; логин; пароль;)!")
                
    if msg.lower() in mailcommands:
        write_admin(event.user_id, "Введите сообщение для отправки или нажмите на кнопку для отмены:", cancelkeyboard)
        last_event = "r"
        
    if last_event == "r" and len(msg) > 1:
        if msg.lower() not in cancelcommands: 
            mail(event.user_id, msg)
        else:
            write_admin(event.user_id, "Рассылка отменена!")
            last_event = "none"
    #Защитный механизм
    elif len(msg) == 1 and last_event == "r":
        write_admin(event.user_id, "Длина сообщения должна быть минимум 2 символа! ('Отмена' для отмены отправки)")
