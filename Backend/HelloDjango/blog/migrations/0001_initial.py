# Generated by Django 3.1.4 on 2021-06-19 13:01

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('miniature', models.URLField(blank=True, null=True, verbose_name='Миниатюра')),
                ('photo', models.URLField(blank=True, null=True, verbose_name='Изображение')),
                ('short_description', models.TextField(help_text='БУдет использоваться в SEO(description)', verbose_name='Краткое описание')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='История болезни')),
                ('public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('public_on_home_page', models.BooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('views', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('direction', models.ManyToManyField(blank=True, related_name='stories', to='clinic.Direction', verbose_name='Направление')),
                ('doctor', models.ManyToManyField(blank=True, related_name='stories', to='clinic.Doctor', verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'История болезни',
                'verbose_name_plural': '2. Истории болезни',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('miniature', models.URLField(blank=True, null=True, verbose_name='Миниатюра новости')),
                ('photo', models.URLField(verbose_name='Изображение новости')),
                ('short_description', models.TextField(help_text='БУдет использоваться в SEO(description)', verbose_name='Краткое описание')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Пост')),
                ('slug', models.SlugField(unique=True)),
                ('public', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('public_on_home_page', models.BooleanField(default=False, verbose_name='Опубликовать на главной')),
                ('actual', models.BooleanField(default=False, verbose_name='Актуальное')),
                ('clinic_life', models.BooleanField(default=False, verbose_name='Жизнь клиники')),
                ('likes', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во лайков')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('views', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('direction', models.ManyToManyField(blank=True, related_name='posts', to='clinic.Direction', verbose_name='Направление')),
                ('doctor', models.ManyToManyField(blank=True, related_name='posts', to='clinic.Doctor', verbose_name='Доктор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': '1. Посты',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название видео')),
                ('url', models.CharField(blank=True, max_length=100, null=True, verbose_name='Код видео')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления видео')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='blog.post', verbose_name='Пост')),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='blog.medicalhistory', verbose_name='История болезни')),
            ],
            options={
                'verbose_name': 'Видео',
                'verbose_name_plural': 'Видео',
            },
        ),
        migrations.CreateModel(
            name='PostReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parents', to='blog.postreviews')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='blog.post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий к посту',
                'verbose_name_plural': '3. Комментарии к постам',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='MedicalHistoryReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('likes', models.PositiveSmallIntegerField(default=0, verbose_name='Кол-во лайков')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Изменен')),
                ('history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='blog.medicalhistory', verbose_name='История болезни')),
            ],
            options={
                'verbose_name': 'Комментарий к истории болезни',
                'verbose_name_plural': '4. Комментарии к историям болезни',
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название изображения')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Alt')),
                ('url', models.URLField(verbose_name='URL изображения')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядковый номер')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='blog.post', verbose_name='Пост')),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='blog.medicalhistory', verbose_name='История болезни')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
