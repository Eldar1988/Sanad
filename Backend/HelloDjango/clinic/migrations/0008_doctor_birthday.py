# Generated by Django 3.1.4 on 2020-12-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_auto_20201208_0539'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]
