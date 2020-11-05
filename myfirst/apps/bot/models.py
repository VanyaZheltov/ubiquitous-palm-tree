from django.db import models
import datetime

class Log(models.Model):
    event = models.TextField('Событие')
    time = models.TimeField(auto_now=True)
    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'

class BotInfo(models.Model):
    confirmation_token = models.CharField('Код подтверждения', max_length = 20)
    token = models.CharField('Токен', max_length = 100)
    group_name = models.TextField('Группа')
    class Meta:
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'