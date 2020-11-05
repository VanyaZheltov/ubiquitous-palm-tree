from __future__ import unicode_literals
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .main_config import *
from django.views.decorators.csrf import csrf_exempt
import json, vk_api
from .models import Log
import random
from .CommandParse import get_answer
from vk_api.utils import get_random_id
from .admin_module import AdminHandler
from .admin_module import write_main

# Create your views here.
def Write_Log(event):
    log = Log()


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