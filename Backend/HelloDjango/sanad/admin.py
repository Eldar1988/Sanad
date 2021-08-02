from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slider, Advantage, Contacts, PhotoGallery, VideoGallery, About, MainInfo, Banner


admin.site.register(Contacts)
admin.site.register(About)
admin.site.register(MainInfo)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'public', 'pub_date', 'update')
    list_display_links = ('get_image', 'title')
    list_editable = ('order', 'public')
    list_filter = ('public', 'pub_date', 'update')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Картинка'

    save_as = True
    save_on_top = True


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'public_on_home', 'public_on_about', 'order', 'pub_date', 'update')
    list_editable = ('order', 'public_on_home', 'public_on_about')
    search_fields = ('title',)
    list_filter = ('public_on_home', 'public_on_about', 'pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" height=50')

    get_image.short_description = 'Фото'


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'icon')
    list_editable = ('order', 'icon')
    search_fields = ('title',)
    save_as = True
    save_on_top = True


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'url', 'order', 'date', 'update')
    list_editable = ('order',)
    list_filter = ('date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image}" height=50')

    get_image.short_description = 'Баннер'
