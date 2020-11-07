from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Item, IndexSlide, Article
import json
import vk_api
import uuid
from yandex_checkout import Configuration, Payment
Configuration.account_id = 673499
Configuration.secret_key = 'live_wcXpppdnx57D4iTUcqQr_fYwXFlLad0v7Rh1-9N2mU4'

class Result:
    def __init__(self, amount, description, status):
        self.amount = amount
        self.description = description
        self.status = status


def index(request):
    cards = Item.objects.all()
    slides = IndexSlide.objects.all()
    lastposts = Article.objects.all().order_by('-id')[:3]
    return render(request, 'shop/list.html', {'products': cards, 'slides': slides, 'posts': lastposts})
	
def form(request, pr_id):
    try:
        product = Item.objects.get(id=pr_id)
        idempotence_key = str(uuid.uuid4())
        payment = Payment.create({
            "amount": {
            "value": product.price,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "embedded"
        },
        "description": f'{product.name}|EnglishPush'
        }, idempotence_key)	
        conf_token = json.loads(payment.json())['confirmation']['confirmation_token']
        id = json.loads(payment.json())['id']
        return render(request, 'shop/order.html', {'conf_token':conf_token, 'id': id, 'product': product})
    except:
        return render(request, 'shop/product.html')

def result(request, id):
    payment = Payment.find_one(id)
    payment_result = Result(amount=payment.amount, description=payment.description, status=payment.status)
    return render(request, 'shop/result.html', {'result': payment_result})

def article(request, id):
    try:
        post = Article.objects.get(id=id)
        return render(request, 'shop/post.html', {'post': post})
    except:
        return render(request, 'shop/post.html')

def articles(request):
    allarticles = Article.objects.all()
    return render(request, 'shop/posts.html', {'posts': allarticles}) 

def product(request, pr_id):
    try:
        product = Item.objects.get(id=pr_id)
        return render(request, 'shop/product.html', {'product': product})
    except:
        return render(request, 'shop/product.html')