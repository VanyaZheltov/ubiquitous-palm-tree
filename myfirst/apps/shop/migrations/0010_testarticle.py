# Generated by Django 3.1.2 on 2020-11-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_delete_testarticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
        ),
    ]