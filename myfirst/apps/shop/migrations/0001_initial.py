# Generated by Django 3.1.2 on 2020-10-25 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100, verbose_name='Заголовок статьи')),
                ('text', models.TextField(verbose_name='Текст')),
                ('preview', models.ImageField(upload_to='articles', verbose_name='Превью')),
                ('pub_date', models.DateField(auto_now=True, verbose_name='Время публикации')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(max_length=8, verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='shop', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=200, verbose_name='Описание')),
                ('bg_photo', models.ImageField(upload_to='slider', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.article')),
            ],
        ),
    ]
