from django.contrib import admin
from .models import Item, Image, IndexSlide, Article, ArticlePhotos

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
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(IndexSlide, SliderSlideAdmin)