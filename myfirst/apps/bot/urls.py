from django.urls import path
from . import views
import importlib

app_name = 'bot'
urlpatterns = [
	path('', views.Index.as_view(), name = 'index'),
	path('admin/', views.IndexAdmin.as_view(), name = 'admin')

]

