from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Healing, Direction, Action, VideoGallery, ImageGallery, Doctor, DirectionReviews, DoctorReviews


@admin.register(Healing)
class HealingAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('direction',)

    save_on_top = True
    save_as = True


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'is_for_kids_direction', 'order', 'slug', 'views', 'pub_date', 'update')
    list_display_links = ('get_image', 'title')
    list_editable = ('is_for_kids_direction', 'order', 'slug')
    search_fields = ('title',)
    list_filter = ('is_for_kids_direction', 'pub_date', 'update')
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Изображение'


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'update')
    list_filter = ('pub_date', 'update')
    search_fields = ('title',)
    save_on_top = True
    save_as = True


@admin.register(VideoGallery)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('directions', 'doctors', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster}" height=50')

    get_image.short_description = 'Постер'


@admin.register(ImageGallery)
class AdminImage(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('directions', 'doctors', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster}" height=50')

    get_image.short_description = 'Фото'


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'get_image', 'name', 'public', 'public_on_home_page', 'order', 'slug', 'views', 'pub_date', 'update')
    list_editable = ('public_on_home_page', 'order', 'slug', 'public')
    list_display_links = ('get_image', 'name')
    list_filter = ('direction', 'pub_date', 'update')
    search_fields = ('name',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'


@admin.register(DirectionReviews)
class DirectionReviewsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'direction', 'public', 'rating', 'public_on_home_page', 'order', 'pub_date', 'update')
    list_filter = ('direction', 'rating', 'public_on_home_page', 'pub_date', 'update')
    list_editable = ('rating', 'public_on_home_page', 'order', 'public')
    list_display_links = ('get_image', 'name')
    search_fields = ('name',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'


@admin.register(DoctorReviews)
class DoctorReviewsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'doctor', 'public', 'rating', 'public_on_home_page', 'order', 'pub_date', 'update')
    list_filter = ('doctor', 'rating', 'public_on_home_page', 'pub_date', 'update')
    list_editable = ('rating', 'public_on_home_page', 'order', 'public')
    list_display_links = ('get_image', 'name')
    search_fields = ('name',)
    save_on_top = True
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar}" height=50')

    get_image.short_description = 'Аватар'
