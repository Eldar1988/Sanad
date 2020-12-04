from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Healing(models.Model):
    """Методы и этапы лечения"""
    title = models.CharField('Заголовок этапа', max_length=255)
    description = RichTextUploadingField('Описание')
    order = models.PositiveSmallIntegerField('Порядковый номер')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Этап лечения'
        verbose_name_plural = 'Этапы лечения'
        ordering = ('order',)


class Direction(models.Model):
    """Медицинские направления"""
    is_for_kids_direction = models.BooleanField('Детское направление', default=False)
    title = models.CharField('Название направления', max_length=255)
    image = models.URLField('Изображение')
    short_description = models.TextField('Краткое описание',
                                         help_text='Будет использоваться также в SEO (description)')
    description = RichTextUploadingField('Полное описание')
    stages_of_treatment = models.ManyToManyField(Healing, related_name='stages_of_treatment', blank=True,
                                                 verbose_name='Этапы лечения')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField('Дата создания направления в базе', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)
    views = models.PositiveSmallIntegerField('Кол-во просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Медицинское направление'
        verbose_name_plural = 'Медицинские направления'
        ordering = ('order',)


class Action(models.Model):
    """Акции"""
    title = models.CharField('Заголовок акции', max_length=255)
    short_description = models.TextField('Краткое описание')
    description = RichTextUploadingField('Полное описание', null=True, blank=True)
    pub_date = models.DateTimeField('Дата создания акции', auto_now_add=True)
    update = models.DateTimeField('Дата изменения акции', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = ' Акции'


class Video(models.Model):
    """Видео ролики"""
    title = models.CharField('Название видео', max_length=255)
    url = models.URLField('URL видео')
    order = models.PositiveSmallIntegerField('Порядковый номер')
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
    url = models.URLField('URL изображения')
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата добавления', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Doctor(models.Model):
    """Доктор"""
    direction = models.ManyToManyField(Direction, blank=True, verbose_name='Направления', related_name='directions')
    name = models.CharField('Имя доктора', max_length=255)
    photo = models.URLField('Фото (фон на странице доктора')
    avatar = models.URLField('Аватар доктора', default='https://res.cloudinary.com/space-developers/image/upload/v1607059811/Sanad/undraw_profile_pic_ic5t_qvsdyi.svg')
    short_description = models.TextField('Короткое описание', help_text='Будет использоваться в SEO')
    description = RichTextUploadingField('Полное описание')
    action = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True, blank=True, related_name='actions',
                               verbose_name='Акции')
    video = models.ManyToManyField(Video, blank=True, related_name='video', verbose_name='Видео врача')
    photos = models.ManyToManyField(Image, null=True, blank=True, verbose_name='photos', related_name='Изображения')
    say = RichTextUploadingField('Слово специалиста')
    public_on_home_page = models.BooleanField('Опубликовать на главной странице сайта', default=False)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField('Дата создания врача в базе', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)
    views = models.PositiveSmallIntegerField('Количество просмотров страницы врача')

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.name


class DirectionReviews(models.Model):
    """Отзывы к направлениям"""
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True,
                                  verbose_name='Медицинское направление',
                                  related_name='direction')
    name = models.CharField('Имя', max_length=255)
    avatar = models.URLField('Фото', default='https://res.cloudinary.com/space-developers/image/upload/v1607059811/Sanad/undraw_profile_pic_ic5t_qvsdyi.svg')
    text = RichTextUploadingField('Отзыв')
    video = models.URLField('Ссылка на видео (необязательно)', blank=True, null=True)
    rating = models.PositiveSmallIntegerField('Оценка (от 1 до 5)', default=5)
    public_on_home_page = models.BooleanField('Опубликовать на главной странице сайта', default=False)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата создания отзыва', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв к направлению'
        verbose_name_plural = 'Отзывы к направлениям'


class DoctorReviews(models.Model):
    """Отзывы к докторам"""
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor',
                               verbose_name='Доктор')
    name = models.CharField('Имя', max_length=255)
    avatar = models.URLField('Фото', default='https://res.cloudinary.com/space-developers/image/upload/v1607059811/Sanad/undraw_profile_pic_ic5t_qvsdyi.svg')
    text = RichTextUploadingField('Отзыв')
    video = models.URLField('Ссылка на видео (необязательно)', blank=True, null=True)
    rating = models.PositiveSmallIntegerField('Оценка (от 1 до 5)', default=5)
    public_on_home_page = models.BooleanField('Опубликовать на главной странице сайта', default=False)
    order = models.PositiveSmallIntegerField('Порядковый номер')
    pub_date = models.DateTimeField('Дата создания отзыва', auto_now_add=True)
    update = models.DateTimeField('Дата изменения', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв к направлению'
        verbose_name_plural = 'Отзывы к направлениям'








