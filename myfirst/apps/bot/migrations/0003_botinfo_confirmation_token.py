# Generated by Django 3.1.2 on 2020-10-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_botinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='botinfo',
            name='confirmation_token',
            field=models.TextField(default=0, verbose_name='Код подтверждения'),
            preserve_default=False,
        ),
    ]
