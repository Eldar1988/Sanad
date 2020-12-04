from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Video, Image, Post, MedicalHistory, PostReviews, MedicalHistoryReviews


@admin.register(PostReviews)
class PostReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'text', 'public', 'pub_date', 'update')
    list_editable = ('public',)
    search_fields = ('name', 'text')
    list_filter = ('pub_date', 'update', 'post', 'public')
    save_as = True
    save_on_top = True


@admin.register(MedicalHistoryReviews)
class MedicalHistoryReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'history', 'text', 'public', 'pub_date', 'update')
    list_editable = ('public',)
    search_fields = ('name', 'text')
    list_filter = ('pub_date', 'update', 'history', 'public')
    save_as = True
    save_on_top = True


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'doctor', 'direction', 'public', 'is_action', 'is_news', 'public_on_home_page',
                    'slug', 'order', 'views', 'pub_date', 'update')
    list_editable = ('doctor', 'direction', 'is_action', 'is_news', 'public_on_home_page', 'slug', 'order', 'public')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    list_filter = ('doctor', 'direction', 'is_action', 'is_news', 'public_on_home_page', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Фото'


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'doctor', 'direction', 'public_on_home_page', 'public_on_home_page',
                    'slug', 'order', 'views', 'pub_date', 'update')
    list_editable = ('doctor', 'direction', 'public_on_home_page', 'slug', 'order')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    list_filter = ('doctor', 'direction', 'public_on_home_page', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Фото'



