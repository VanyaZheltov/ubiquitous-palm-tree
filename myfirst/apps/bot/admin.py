from django.contrib import admin
from .models import Log, BotInfo

class LogAdmin(admin.ModelAdmin):
    list_display = ('time', 'event')
    
class InfoAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'confirmation_token')

admin.site.register(BotInfo, InfoAdmin)
admin.site.register(Log, LogAdmin)
