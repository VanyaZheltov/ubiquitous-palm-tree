from django.contrib import admin
from .models import Dialog

class PostAdmin(admin.ModelAdmin):  
    list_display = ('question', 'answer') 

admin.site.register(Dialog, PostAdmin)
