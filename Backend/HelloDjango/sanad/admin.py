from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slider, Advantage, Contacts, Social, PhotoGallery, VideoGallery, About


admin.site.register(Contacts)
admin.site.register(Social)
admin.site.register(About)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'button_text', 'order', 'public', 'pub_date', 'update')
    list_editable = ('button_text', 'order', 'public')
    list_filter = ('public', 'pub_date', 'update')

    save_as = True
    save_on_top = True


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.url}" height=50')

    get_image.short_description = 'Постер'


@admin.register(VideoGallery)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'order', 'pub_date', 'update')
    list_editable = ('order',)
    search_fields = ('title',)
    list_filter = ('pub_date', 'update')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster}" height=50')

    get_image.short_description = 'Постер'


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'icon')
    list_editable = ('order', 'icon')
    search_fields = ('title',)
    save_as = True
    save_on_top = True
