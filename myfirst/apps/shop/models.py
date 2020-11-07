from django.db import models
from django.utils import timezone
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Item(models.Model):
    name = models.CharField('Наименование', max_length = 100)
    description = models.TextField('Описание')
    price = models.CharField('Цена', max_length = 8)
    photo = models.ImageField("Фото", upload_to="shop")
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Image(models.Model):
    image = models.ImageField(upload_to="shop")
    file = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="images") 
    
class IndexSlide(models.Model):
    header = models.CharField("Заголовок", max_length = 20)
    description = models.CharField("Описание", max_length = 200)
    bg_photo = models.ImageField("Фото", upload_to="slider")
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
    
class Article(models.Model):
    header = models.CharField("Заголовок статьи", max_length = 100)
    text = models.TextField("Текст")
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    preview = models.ImageField("Превью", upload_to="articles", blank=True)
    pub_date = models.DateField("Время публикации", auto_now = True)
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-pub_date',)

class ArticlePhotos(models.Model):
    image = models.ImageField(upload_to="articles")
    file = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="images") 

