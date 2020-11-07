from __future__ import unicode_literals
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .main_config import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json, vk_api
from .models import Log
import random
from .CommandParse import get_answer
from vk_api.utils import get_random_id
from .admin_module import AdminHandler
from .admin_module import write_main
from datetime import datetime
import requests
from shop.models import Article
from aiogram import Bot, Dispatcher, types
import asyncio




# Create your views here.
def Write_Log(event):
    log = Log()

#r = request.get(f"127.0.0.1/posts/?header=test&text=test&author=admin&preview={"https://sun9-19.userapi.com/impf/F5ZlJKuA-3_fYRyhiFwsb4vYCLhOQwzsj8RVpg/0CXx54KhU7Y.jpg?size=500x409&quality=96&proxy=1&sign=a50c89429d6e5363a689c81d1927aad7&c_uniq_tag=Wvr_UGnoZ6cFsZ-H1izH4zZGQhf4FrWT-jZfuI2.jpg"}&key=HKEYCURRADMIN")

class Index(APIView):
    def get(self, request):
        return HttpResponse("Здесь ничего нет :)")
    def post(self, request):
        data = json.loads(request.body)
        if (data['secret'] == secret_key):# if json request contain secret key and it's equal my secret key
            if (data['type'] == 'confirmation'):# if VK server request confirmation
                p = Log(event="confirmation")
                p.save()
                return HttpResponse(confirmation_token, content_type="text/plain", status=200)
            if (data['type'] == 'message_new'):
                user_id = data['object']['user_id']
                answer = get_answer(data['object']['body'])
                write_main(user_id, answer)
                p = Log(event="new message")
                p.save()
                return HttpResponse('ok', content_type="text/plain", status=200)
            if (data['type'] == 'wall_post_new'):
                article_text = data['object']['text']
                time = datetime.fromtimestamp(data['object']['date'])
                try:
                    if data['object']['attachments'] != None:
                        if type(data['object']['attachments']) == list:
                            preview = data['object']['attachments'][0]['photo']['photo_604'] 
                        else:
                            preview = data['object']['attachments']['photo']['photo_604'] 
                    else:
                        preview = "None"
                except:
                    preview = "None"
                
                p = Article(header=f"Новости от {datetime.now()}", text=article_text, author=User.objects.get(username="admin"), preview=preview + '.jpg')
                p.save()
                return HttpResponse('ok', content_type="text/plain", status=200)


                

class IndexAdmin(APIView):
    def get(self, request):
        return HttpResponse("Здесь ничего нет :)")
    def post(self, request):
        data = json.loads(request.body)
        if (data['secret'] == secret_key):# if json request contain secret key and it's equal my secret key
            if (data['type'] == 'confirmation'):# if VK server request confirmation
                return HttpResponse(admin_conf_token, content_type="text/plain", status=200)
            if (data['type'] == 'message_new'):
                user_id = data['object']['user_id']
                message = data['object']['body']
                AdminHandler(user_id, message)
                return HttpResponse('ok', content_type="text/plain", status=200)