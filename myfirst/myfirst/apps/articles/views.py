from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Dialog
import random

def index(request):
	testdata = [str(word)
				for word in range(5)]
	return render(request, 'articles/list.html', {'data':testdata})

def detail(request):
	try:
		commands = {

		}
		return render(request, 'articles/detail.html', {'commands': commands})
	except:
		raise Http404("Статья не найдена! :-<")

	
