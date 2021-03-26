from rest_framework import serializers
from .models import Post, PostReviews, MedicalHistory, MedicalHistoryReviews, Video, Image


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        models = Post
        fields = ('id', 'title', 'miniature', 'slug')


class MedicalStoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ('id', 'title', 'miniature', 'slug')


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'url')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'title', 'alt', 'url')


class PostDetailSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class MedicalHistoryDetailView(serializers.ModelSerializer):
    videos = VideoSerializer(many=True)
    images = ImageSerializer(many=True)

    class Meta:
        model = MedicalHistory
        fields = '__all__'




