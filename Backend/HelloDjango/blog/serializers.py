from rest_framework import serializers
from .models import Post, PostReviews, MedicalHistory


class PostReviewListSerializer(serializers.ModelSerializer):
    """Комментарии к посту"""
    class Meta:
        model = PostReviews
        fields = ('id',)


class PostDetailReviewsSerializer(serializers.ModelSerializer):
    """Комментари к посту (детали)"""
    class Meta:
        model = PostReviews
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    """Страница поста"""

    class Meta:
        model = Post
        exclude = ('doctor', 'direction', 'public_on_home_page', 'order', 'update', 'public')


class PostSerializer(serializers.ModelSerializer):
    """Истории болезни"""
    reviews = PostReviewListSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('pub_date', 'update', 'doctor', 'direction', 'order', 'body', 'public_on_home_page')


class HistoryDetailSerializer(serializers.ModelSerializer):
    """Страница истории"""

    class Meta:
        model = Post
        exclude = ('doctor', 'direction', 'public_on_home_page', 'order', 'update', 'public')