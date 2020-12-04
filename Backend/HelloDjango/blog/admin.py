from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Video, Image, Post, MedicalHistory, PostReviews, MedicalHistoryReviews

admin.site.register(PostReviews)
admin.site.register(MedicalHistoryReviews)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    list_display = ('title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'doctor', 'direction', 'is_action', 'is_news', 'public_on_home_page',
                    'slug', 'order', 'views', 'pub_date', 'update')
    list_editable = ('doctor', 'direction', 'is_action', 'is_news', 'public_on_home_page', 'slug', 'order')
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
    list_display = ('get_image', 'title', 'doctor', 'direction', 'public_on_home_page',
                    'slug', 'order', 'views', 'pub_date', 'update')
    list_editable = ('doctor', 'direction', 'public_on_home_page', 'slug', 'order')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    list_filter = ('doctor', 'direction', 'is_action', 'is_news', 'public_on_home_page', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Фото'



