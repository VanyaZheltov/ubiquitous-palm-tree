from django.urls import path
from . import views
import importlib


app_name = 'shop'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('order/<int:pr_id>/', views.form, name='order'),
	path('order/result/<str:id>/', views.result, name='result'),
	path('product/<int:pr_id>/', views.product, name='product'),
	path('posts/post/<int:id>/', views.article, name='post'),
	path('posts/', views.articles, name='posts')
]