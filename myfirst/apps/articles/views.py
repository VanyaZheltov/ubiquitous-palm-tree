from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .models import Dialog
from django.views.generic import TemplateView
import uuid
import random
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .serializers import DialogSerializer
from rest_framework.renderers import JSONRenderer
import json
from yandex_checkout import Configuration, Payment

Configuration.account_id = 673499
Configuration.secret_key = 'live_wcXpppdnx57D4iTUcqQr_fYwXFlLad0v7Rh1-9N2mU4'

def index(request):
	return render(request, 'articles/list.html')

def detail(request):
    commands = Dialog.objects.all()
    cmds = {command.question : command.answer
        for command in commands
    }
    return render(request, 'articles/detail.html', {'commands': cmds})

def order(request):
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
        "value": "1.00",
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url":"https://merchant.site/"
        },
        "capture": True,
        "description": "Zakaz",
        "test": "true"
    }, idempotence_key)
    confirmation_url = json.loads(payment.json())['confirmation']['confirmation_url']
    return render(request, 'articles/order.html', {'confirmation':confirmation_url})
    
def form(request):
    idempotence_key = str(uuid.uuid4())
    payment = Payment.create({
		"amount": {
        "value": "2.00",
        "currency": "RUB"
    },
    "confirmation": {
        "type": "embedded"
    },
    "description": "Заказ №72"
	}, idempotence_key)	
    conf_token = json.loads(payment.json())['confirmation']['confirmation_token']
    id = json.loads(payment.json())['id']
    return render(request, 'shop/order.html', {'conf_token':conf_token, 'id': id})

def result(request):
    id = request.GET.get("id", 0)
    payment = Payment.find_one(id)
    return HttpResponse(payment.json())

