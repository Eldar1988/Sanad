# Generated by Django 3.1.4 on 2021-06-23 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0005_auto_20210623_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videogallery',
            old_name='url',
            new_name='video',
        ),
    ]
