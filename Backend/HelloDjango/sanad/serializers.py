from rest_framework import serializers

from .models import VideoGallery, PhotoGallery, About


class AboutPageSerializer(serializers.ModelSerializer):
    """Страница о клинике"""
    class Meta:
        model = About
        fields = '__all__'


class VideoSanadSerializer(serializers.ModelSerializer):
    """Видео"""
    class Meta:
        model = VideoGallery
        fields = ('id', 'title', 'url')


class PhotoSanadSerializer(serializers.ModelSerializer):
    """Видео"""
    class Meta:
        model = PhotoGallery
        fields = ('id', 'title', 'url')
