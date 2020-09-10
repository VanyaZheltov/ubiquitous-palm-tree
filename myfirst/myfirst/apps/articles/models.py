import datetime
from django.utils import timezone
from django.db import models

class Dialog(models.Model):
	question = models.CharField('Вопрос', max_length = 100)
	answer = models.CharField('Ответ', max_length = 100)
	class Meta:
		verbose_name = 'Диалог'
		verbose_name_plural = 'Диалоги'

