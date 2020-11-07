from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class ArticleForm(forms.ModelForm):
    text = forms.CharField(label="Текст", widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ImageInline(admin.TabularInline):
    model = Image
class ArticleImageInline(admin.TabularInline):
    model = ArticlePhotos

class ItemAdmin(admin.ModelAdmin):  
    list_display = ('name', 'price')
    inlines = [ImageInline]

class SliderSlideAdmin(admin.ModelAdmin):
    list_display = ('header', 'description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('header', 'pub_date')
    form = ArticleForm
    inlines = [ArticleImageInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(IndexSlide, SliderSlideAdmin)
admin.site.site_title="Магазин"
admin.site.site_header="Магазин"