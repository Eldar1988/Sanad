# Generated by Django 3.1.4 on 2021-08-27 20:50

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanad', '0005_auto_20210802_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядковый номер')),
                ('public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Информационная страница',
                'verbose_name_plural': '9. Информационные страницы',
                'ordering': ('-date', 'order'),
            },
        ),
    ]
