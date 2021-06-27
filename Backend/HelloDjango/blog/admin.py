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


class VideosInline(admin.TabularInline):
    model = Video
    fields = ('title', 'url', 'order')
    extra = 0


class ImagesInline(admin.TabularInline):
    model = Image
    fields = ('title', 'alt',  'url', 'order', 'get_image')
    extra = 0
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" height=50')

    get_image.short_description = 'Миниатюра'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'public', 'public_on_home_page', 'clinic_life',
                    'views', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('public_on_home_page', 'title', 'public', 'clinic_life',)
    search_fields = ('title',)
    list_filter = ('doctor', 'direction', 'public_on_home_page', 'pub_date', 'update')
    filter_horizontal = ('doctor', 'direction')
    inlines = [VideosInline, ImagesInline]
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.photo}" height=50')

    get_image.short_description = 'Фото'


@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'public', 'public_on_home_page',
                    'slug', 'views', 'pub_date', 'update')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('public_on_home_page', 'public', 'slug')
    list_display_links = ('get_image', 'title')
    search_fields = ('title',)
    list_filter = ('doctor', 'direction', 'public_on_home_page', 'pub_date', 'update')
    filter_horizontal = ('doctor', 'direction')
    inlines = [VideosInline, ImagesInline]
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.photo}" height=50')

    get_image.short_description = 'Фото'






