# Generated by Django 3.1.4 on 2020-12-08 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0011_action_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='more_btn',
            field=models.BooleanField(default=False, verbose_name='Кнопка подробнее'),
        ),
    ]
