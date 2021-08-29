from rest_framework import serializers

from .models import VideoGallery, PhotoGallery, About, MainInfo, Slider, Advantage, Contacts, Banner, InfoPage


class InfoPageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPage
        fields = ('id', 'title', 'slug')


class InfoPageDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPage
        fields = '__all__'


class MainInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainInfo
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ('pub_date', 'order', 'update')


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class AboutPageSerializer(serializers.ModelSerializer):
    """Страница о клинике"""
    class Meta:
        model = About
        fields = '__all__'


class VideoSanadSerializer(serializers.ModelSerializer):
    """Видео"""
    class Meta:
        model = VideoGallery
        fields = ('id', 'title', 'url', 'image')


class PhotoSanadSerializer(serializers.ModelSerializer):
    """Видео"""
    class Meta:
        model = PhotoGallery
        fields = ('id', 'title', 'url')


class BannerSerializer(serializers.ModelSerializer):
    """Баннеры"""
    class Meta:
        model = Banner
        fields = ('id', 'image', 'url')
