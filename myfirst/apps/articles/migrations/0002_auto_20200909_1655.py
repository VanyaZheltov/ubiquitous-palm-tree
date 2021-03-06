# Generated by Django 3.1.1 on 2020-09-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer', models.CharField(max_length=100, verbose_name='Ответ')),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
