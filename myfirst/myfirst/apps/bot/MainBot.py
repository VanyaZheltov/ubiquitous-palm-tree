import time
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import requests
from . import CommandParse


token = "f9226fd7da439e5e4a443d2cab203c527fc5db6c13568d32c795128f4e88e79593fee5191215dc47aed2d"
vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

def write_msg(user_id, message, keyboard = None, attachment = None):
    vk.method('messages.send', {'user_id': user_id, 'message': message,'keyboard': keyboard if keyboard != None else [],"attachment": attachment if attachment != None else None, 'random_id': random.randint(0,11111)})


def start_main():

    #StartServer()

    print('Основной Бот запущен')

    for event in longpoll.listen(): #Прослушивание сервера ВК

        if event.type == VkEventType.MESSAGE_NEW:

            if event.to_me:

                msg = event.text
                print(event.user_id) #Сам ответ
                if msg != "test":
                    write_msg(event.user_id, CommandParse.get_answer(event.text.lower()))
                else:
                    pass
                