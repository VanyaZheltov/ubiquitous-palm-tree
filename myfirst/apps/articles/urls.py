from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('cmds/', views.detail, name = 'detail'),
	path('order/', views.order, name='order'),
	path('order/form/', views.form, name='form'),
	path('order/result/', views.result, name='result')
]