# Generated by Django 3.1.4 on 2020-12-07 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20201207_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='rating',
        ),
    ]
