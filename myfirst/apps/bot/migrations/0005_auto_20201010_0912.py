# Generated by Django 3.1.2 on 2020-10-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_auto_20201009_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='botinfo',
            name='token',
            field=models.CharField(max_length=100, verbose_name='Токен'),
        ),
    ]
