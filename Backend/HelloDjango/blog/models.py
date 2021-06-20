from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from clinic.models import Doctor, Direction


class Post(models.Model):
    """Пост"""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(unique=True)
    miniature = models.URLField('Миниатюра новости', null=True, blank=True)
    photo = models.URLField('Изображение новости')
    short_description = models.TextField('Краткое описание', help_text='БУдет использоваться в SEO(description)')
    body = RichTextUploadingField('Пост')
    doctor = models.ManyToManyField(Doctor, blank=True, verbose_name='Доктор', related_name='posts')
    direction = models.ManyToManyField(Direction, blank=True, verbose_name='Направление', related_name='posts')
    public = models.BooleanField('Опубликовать', default=True)
    public_on_home_page = models.BooleanField('Опубликовать на главной', default=False)
    actual = models.BooleanField('Актуальное', default=False)
    clinic_life = models.BooleanField('Жизнь клиники', default=False)
    likes = models.PositiveSmallIntegerField('Кол-во лайков', default=0)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)
    views = models.PositiveSmallIntegerField('Кол-во просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = '1. Посты'
        ordering = ('-pub_date',)


class PostReviews(models.Model):
    """Комментарии к постам"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Комментарий')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True,
                             verbose_name='Пост', related_name='reviews')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='parents')
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий к посту'
        verbose_name_plural = '3. Комментарии к постам'
        ordering = ('-pub_date',)


class MedicalHistory(models.Model):
    """История болезни"""
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField(unique=True)
    miniature = models.URLField('Миниатюра', null=True, blank=True)
    photo = models.URLField('Изображение', blank=True, null=True)
    short_description = models.TextField('Краткое описание', help_text='БУдет использоваться в SEO(description)')
    body = RichTextUploadingField('История болезни')
    doctor = models.ManyToManyField(Doctor, blank=True, verbose_name='Доктор', related_name='stories')
    direction = models.ManyToManyField(Direction, blank=True, verbose_name='Направление', related_name='stories')
    public = models.BooleanField('Опубликовать', default=True)
    public_on_home_page = models.BooleanField('Опубликовать на главной', default=False)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)
    views = models.PositiveSmallIntegerField('Кол-во просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'История болезни'
        verbose_name_plural = '2. Истории болезни'
        ordering = ('-pub_date',)


class MedicalHistoryReviews(models.Model):
    """Комментарии к истории болезни"""
    name = models.CharField('Имя', max_length=255)
    text = models.TextField('Комментарий')
    history = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True, blank=True,
                                verbose_name='История болезни', related_name='reviews')
    public = models.BooleanField('Опубликовать', default=False)
    likes = models.PositiveSmallIntegerField('Кол-во лайков', default=0)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий к истории болезни'
        verbose_name_plural = '4. Комментарии к историям болезни'
        ordering = ('-pub_date',)


class Video(models.Model):
    """Видео ролики"""
    title = models.CharField('Название видео', max_length=255)
    url = models.CharField('Код видео', max_length=100, null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    story = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='История болезни', related_name='videos')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост',
                             related_name='videos')
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
    story = models.ForeignKey(MedicalHistory, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='История болезни', related_name='images')
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Пост',
                             related_name='images')
    pub_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
