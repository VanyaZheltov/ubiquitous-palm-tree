from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Dialog
import random



def index(request):
	commands = Dialog.objects.all()
	return render(request, 'articles/list.html', {'commands': commands})

def detail(request):
	try:
		commands = Dialog.objects.all()
		commands = {
		command.question: command.answer
		for command in commands
		}
		return render(request, 'articles/detail.html', {'commands': commands})
	except:
		raise Http404("Статья не найдена! :-<")

	
