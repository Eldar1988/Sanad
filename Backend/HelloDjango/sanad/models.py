from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class MainInfo(models.Model):
    """Информация для шапки сайта"""
    title = models.CharField('Title сайта (главная страница)', max_length=255)
    description = models.TextField('Description сайта (главная страница)')
    news_title = models.CharField('Заголовок для страницы новостей', max_length=255, blank=True, null=True)
    news_image = models.URLField('Картинка для страницы новостей', null=True, blank=True)
    news_description = models.TextField('Краткое описание страницы новостей', blank=True, null=True)
    action_title = models.CharField('Заголовок для страницы акций', max_length=255, null=True, blank=True)
    action_image = models.URLField('Картинка для страницы акций', null=True, blank=True)
    action_description = models.TextField('Краткое описание страницы акций', max_length=255, null=True, blank=True)
    contacts_title = models.CharField('Заголовок для страницы контактов', max_length=255, null=True, blank=True)
    contacts_description = models.TextField('Краткое описание страницы контактов', max_length=255, null=True,
                                            blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовки страниц'
        verbose_name_plural = '2. Заголовки страниц'


class Slider(models.Model):
    """Слайдеры на главной страницы"""
    title = models.CharField('Заголовок слайда', max_length=255)
    title_2 = models.CharField('Заголовок слайда 2', max_length=255, null=True, blank=True)
    image = models.URLField('Картинка', null=True, blank=True)
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)
    public = models.BooleanField('Опубликовать', default=False)
    pub_date = models.DateTimeField('Дата публикации слайда', auto_now_add=True)
    update = models.DateTimeField('Изменен', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = '3. Слайды'
        ordering = ('order',)


class Advantage(models.Model):
    """Преимущества клиники"""
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст')
    icon = models.CharField('Иконка', max_length=255, help_text='https://material.io/resources/icons/?style=baseline')
    order = models.PositiveSmallIntegerField('Порядковый номер', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = '4. Преимущества'
        ordering = ('order',)


class Contacts(models.Model):
    """Конактная информация"""
    title = models.CharField('Заголвок для страницы контактов', max_length=255)
    text = models.TextField('Подзаголовок', null=True, blank=True)
    phones = models.CharField('Телефоны', max_length=150, help_text='Перечислить через запятую', null=True, blank=True)
    whatsapp = models.CharField('Whatsapp(в формате 7702xxxxxxxx)', max_length=20, blank=True, null=True,
                                help_text='просто 7 вместо 8 или +7')
    address = models.TextField('Адрес клиники')
    frame = models.TextField('Frame карты', null=True, blank=True)
    work_time = RichTextUploadingField('Время работы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = '5. Контакты'


class Social(models.Model):
    """Социальные сети"""
    title = models.CharField('Название соцсети', max_length=255)
    icon = models.CharField('Иконка', max_length=255, help_text='https://material.io/resources/icons/?style=baseline')
    url = models.URLField('Ссылка на страницу в сети')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Социальная сети'
        verbose_name_plural = '6. Социальные сеть'
        ordering = ('order',)


class About(models.Model):
    """О клинике"""
    title = models.CharField('Заголовок страцниы о клинике', max_length=255)
    sub_title = models.CharField('Подзаголовок', max_length=255)
    image = models.URLField('Изображение для страницы о нас', null=True, blank=True)
    text = RichTextUploadingField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О клинике'
        verbose_name_plural = '1. О клинике'


class VideoGallery(models.Model):
    """Видео галерея"""
    public_on_home = models.BooleanField('Показать на главной', default=False)
    title = models.CharField('Название видео', max_length=255)
    url = models.CharField('Код видео', null=True, blank=True, max_length=100)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата добавления видео', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = '7. Видео галерея'


class PhotoGallery(models.Model):
    """Фото галерея"""
    public_on_home = models.BooleanField('Показать на главной', default=False)
    public_on_about = models.BooleanField('Показать на странице о клинике', default=False)
    title = models.CharField('Название фото', max_length=255)
    url = models.URLField('URL фото')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата добавления видео', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = '8. Фото галерея'
