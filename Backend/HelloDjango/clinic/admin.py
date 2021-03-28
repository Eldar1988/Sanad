from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Healing, Direction, Action, VideoGallery, ImageGallery, Doctor, DoctorReviews, \
    Certificate


class HealingInline(admin.TabularInline):
    model = Healing
    fields = ('title', 'description', 'order')
    classes = ('collapse',)
    extra = 0


class ImagesInline(admin.TabularInline):
    model = ImageGallery
    fields = ('title', 'url', 'order', 'get_image')
    extra = 0
    classes = ('collapse',)
    verbose_name_plural = 'Дополнительные фото'

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" height=50')

    get_image.short_description = 'Миниатюра'


class VideosInline(admin.TabularInline):
    model = VideoGallery
    fields = ('title', 'url', 'order')
    extra = 0
    classes = ('collapse',)


class CertificateInline(admin.TabularInline):
    model = Certificate
    fields = ('title', 'image', 'get_image')
    extra = 0
    classes = ('collapse',)
    verbose_name_plural = 'Сертификаты и грамоты доктора'
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Миниатюра'


class DoctorReviewsInline(admin.StackedInline):
    model = DoctorReviews
    fields = ('name', 'avatar', 'text', 'video', 'rating', 'public_on_home_page', 'public')
    extra = 0
    classes = ('collapse',)
    readonly_fields = ('get_image',)
    verbose_name_plural = 'Отзывы о докторе'

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'


@admin.register(DoctorReviews)
class DoctorReviewsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'rating', 'public_on_home_page', 'public', 'pub_date')
    list_editable = ('public_on_home_page', 'public')
    search_fields = ('name', 'text', 'doctor__name')
    list_filter = ('pub_date', 'update')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'is_for_kids_direction', 'order', 'slug', 'views', 'pub_date', 'update')
    list_display_links = ('get_image', 'title')
    list_editable = ('is_for_kids_direction', 'order', 'slug')
    search_fields = ('title',)
    list_filter = ('is_for_kids_direction', 'pub_date', 'update')
    inlines = [HealingInline, ImagesInline, VideosInline]
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Изображение'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'get_image', 'name', 'public', 'public_on_home_page', 'order', 'views', 'pub_date')
    list_editable = ('public_on_home_page', 'order', 'public')
    list_display_links = ('get_image', 'name')
    list_filter = ('directions', 'pub_date', 'update')
    search_fields = ('name', 'directions__title')
    filter_horizontal = ('directions',)
    save_on_top = True
    save_as = True
    inlines = [ImagesInline, VideosInline, CertificateInline, DoctorReviewsInline]

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'show_on_home_page', 'pub_date', 'update')
    list_editable = ('show_on_home_page',)
    list_filter = ('doctors', 'directions', 'show_on_home_page', 'pub_date', 'update')
    search_fields = ('title', 'doctor__name', 'directions__title')
    filter_horizontal = ('doctors', 'directions')
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Изображение'

