# Generated by Django 3.1.4 on 2021-06-23 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0006_auto_20210623_0726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagegallery',
            old_name='url',
            new_name='source',
        ),
    ]
