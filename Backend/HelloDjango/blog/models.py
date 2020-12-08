from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from clinic.models import Doctor, Direction


class Post(models.Model):
    """Пост"""
    title = models.CharField('Заголовок', max_length=255)
    photo = models.URLField('Изображение новости')
    is_action = models.BooleanField('Акция', default=False)
    is_news = models.BooleanField('Новость клиники', default=False)
    public_on_home_page = models.BooleanField('Опубликовать на главной', default=False)
    short_description = models.TextField('Краткое описание', help_text='БУдет использоваться в SEO(description)')
    body = RichTextUploadingField('Пост')
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Доктор')
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Направление')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)
    views = models.PositiveSmallIntegerField('Кол-во просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('order',)


class PostReviews(models.Model):
    """Комментарии к постам"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Комментарий')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пост')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = 'Комментарии к постам'
        ordering = ('-pub_date',)


class MedicalHistory(models.Model):
    """История болезни"""
    title = models.CharField('Заголовок', max_length=255)
    photo = models.URLField('Изображение', blank=True, null=True)
    public_on_home_page = models.BooleanField('Опубликовать на главной', default=False)
    short_description = models.TextField('Краткое описание', help_text='БУдет использоваться в SEO(description)')
    body = RichTextUploadingField('История болезни')
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='Доктор')
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Направление')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)
    views = models.PositiveSmallIntegerField('Кол-во просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История болезни'
        verbose_name_plural = 'Истории болезни'
        ordering = ('order',)


class MedicalHistoryReviews(models.Model):
    """Комментарии к истории болезни"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Комментарий')
    history = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='История болезни')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий к истории болезни'
        verbose_name_plural = 'Комментарии к историям болезни'
        ordering = ('-pub_date',)


class Video(models.Model):
    """Видео ролики"""
    title = models.CharField('Название видео', max_length=255)
    url = models.URLField('URL видео')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    story = models.ManyToManyField(MedicalHistory, blank=True, verbose_name='История болезни')
    post = models.ManyToManyField(Post, blank=True, verbose_name='Пост')
    pub_date = models.DateTimeField('Дата добавления видео', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Image(models.Model):
    """Картинки"""
    title = models.CharField('Название изображения', max_length=255)
    alt = models.CharField('Alt', blank=True, null=True, max_length=255)
    url = models.URLField('URL изображения')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    story = models.ManyToManyField(MedicalHistory, blank=True, verbose_name='История болезни')
    post = models.ManyToManyField(Post, blank=True, verbose_name='Пост')
    pub_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'