from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Slider(models.Model):
    """Слайдеры на главной страницы"""
    title = models.CharField('Заголовок слайда', max_length=255)
    text = models.TextField('Текст на слайдере')
    button_text = models.CharField('Текст на кнопке', max_length=30, default='Подробнее')
    button_url = models.URLField('Ссылка на кнопке', null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации слайда', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ('order',)


class Advantage(models.Model):
    """Преимущества клиник"""
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    icon = models.CharField('Иконка', max_length=255, help_text='https://material.io/resources/icons/?style=baseline')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'
        ordering = ('order',)


class Contacts(models.Model):
    """Конактная информация"""
    title = models.CharField('Заголвок для страницы контактов', max_length=255)
    text = models.TextField('Подзаголовок (необязательно)', null=True, blank=True)
    phone = models.CharField('Телефон 1', max_length=20)
    phone_2 = models.CharField('Телефон 2 (необзяательно)', max_length=20, blank=True, null=True)
    address = models.TextField('Адрес клиники')
    work_time = RichTextUploadingField('Время работы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Social(models.Model):
    """Социальные сети"""
    title = models.CharField('Название соцсети', max_length=255)
    icon = models.CharField('Иконка', max_length=255, help_text='https://material.io/resources/icons/?style=baseline')
    url = models.URLField('Ссылка на страницу в сети')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кантакты'
        verbose_name_plural = 'Кантакты'
        ordering = ('order',)


class VideoGallery(models.Model):
    """Видео галерея"""
    title = models.CharField('Название видео', max_length=255)
    url = models.URLField('URL видео')
    poster = models.URLField('Постер видео')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата добавления видео', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео галерея'


class PhotoGallery(models.Model):
    """Фото галерея"""
    title = models.CharField('Название видео', max_length=255)
    url = models.URLField('URL видео')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата добавления видео', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото галерея'


class About(models.Model):
    """О клинике"""
    title = models.CharField('Заголовок страцниы о клинике', max_length=255)
    sub_title = models.CharField('Подзаголовок', max_length=255)
    text = RichTextUploadingField('Описание')
    videos = models.ManyToManyField(VideoGallery, blank=True, verbose_name='Видео галерея')
    photos = models.ManyToManyField(PhotoGallery, blank=True, verbose_name='Фото галерея')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О клинике'
        verbose_name_plural = 'О клинике'




