# Generated by Django 3.1.4 on 2021-06-25 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0008_auto_20210625_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direction',
            name='image',
        ),
    ]
