from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from sanad.models import MainInfo, Slider, Contacts, About, VideoGallery, PhotoGallery
from sanad.serializers import AboutPageSerializer, VideoSanadSerializer, PhotoSanadSerializer
from clinic.models import Direction, Doctor, Healing, DirectionReviews
from blog.models import MedicalHistory, Post, PostReviews
from blog.serializers import PostDetailReviewsSerializer, PostDetailSerializer, PostSerializer

from .serializers import MainInfoSerializer, SliderSerializer, DirectionListSerializer, DirectionDetailSerializer, \
    DoctorsListSerializer, HealingSerializer, DirectionReviewsSerializer, MedicalHistorySerializer, ContactsSerializer, \
    DoctorsDetailSerializer


class HomePageView(APIView):
    """Информация для главной страницы"""

    def get(self, request):
        response_data = []

        # Заголовки
        info = MainInfo.objects.last()
        info_serializer = MainInfoSerializer(info, many=False)
        response_data.append(info_serializer.data)  # 0 index - Логотип, title, description

        # Слайды
        slides = Slider.objects.filter(public=True)
        slides_serializer = SliderSerializer(slides, many=True)
        response_data.append(slides_serializer.data)  # 1 index - Слайды

        # Направления взросле
        directions = Direction.objects.filter(is_for_kids_direction=False)
        directions_serializer = DirectionListSerializer(directions, many=True)
        response_data.append(directions_serializer.data)  # 2 index - Напрвления взрослые

        # Направления детские
        kids_directions = Direction.objects.filter(is_for_kids_direction=True)
        kids_directions_serializer = DirectionListSerializer(kids_directions, many=True)
        response_data.append(kids_directions_serializer.data)  # 3 index - Напрвления детские

        return Response(response_data)


class DirectionDetailView(APIView):
    """Страница направления"""

    def get(self, request, slug):
        response_data = []

        # Информация о направлении
        direction = Direction.objects.get(slug=slug)
        direction.views += 1
        direction.save()
        direction_serializer = DirectionDetailSerializer(direction, many=False)
        response_data.append(direction_serializer.data)  # 0 index - Инормация о направлении

        # Специалисты направления
        doctors = Doctor.objects.filter(public=True, direction__slug=slug)
        doctors_serializer = DoctorsListSerializer(doctors, many=True)
        response_data.append(doctors_serializer.data)  # 1 index - Специалисты направления

        # Этапы лечения
        healing = Healing.objects.filter(direction__slug=slug)
        healing_serializer = HealingSerializer(healing, many=True)
        response_data.append(healing_serializer.data)  # 2 index - этапы лечения

        # Отзывы
        reviews = DirectionReviews.objects.filter(public=True, direction__slug=slug)
        reviews_serializer = DirectionReviewsSerializer(reviews, many=True)
        response_data.append(reviews_serializer.data)  # 3 index - отзывы

        # Истории болезни
        stories = MedicalHistory.objects.filter(public=True, direction__slug=slug)
        stories_serializer = MedicalHistorySerializer(stories, many=True)
        response_data.append(stories_serializer.data)  # 4 index - Истории болезни

        # Посты
        posts = Post.objects.filter(public=True, direction__slug=slug)
        posts_serializer = PostSerializer(posts, many=True)
        response_data.append(posts_serializer.data)     # 5 index - Посты

        return Response(response_data)


class DoctorDetailView(APIView):
    """Страгица доктора"""

    def get(self, request, slug):
        doctor = Doctor.objects.get(slug=slug)
        doctor.views += 1
        doctor.save()
        serializer = DoctorsDetailSerializer(doctor, many=False)

        return Response(serializer.data)


class ContactsView(APIView):
    """Контактная информация"""

    def get(self, request):
        contacts = Contacts.objects.last()
        serializer = ContactsSerializer(contacts, many=False)
        return Response(serializer.data)


class PostDetailView(APIView):
    """Странцца поста"""

    def get(self, request, slug):
        post_data = []
        post = Post.objects.get(slug=slug)
        post.views += 1
        post.save()
        post_serializer = PostDetailSerializer(post, many=False)
        post_data.append(post_serializer.data)

        if post.is_action:
            posts = Post.objects.filter(public=True, is_action=True).exclude(slug=slug)[:12]
        elif post.is_news:
            posts = Post.objects.filter(public=True, is_news=True).exclude(slug=slug)[:12]
        else:
            posts = Post.objects.filter(public=True, is_news=False, is_action=False).exclude(slug=slug)[:12]
        posts_serializer = PostSerializer(posts, many=True)
        post_data.append(posts_serializer.data)

        return Response(post_data)


class PostDetailReviewsView(APIView):
    """Комментарии к посту (детали)"""
    def get(self, request, slug):
        reviews = PostReviews.objects.filter(post__slug=slug)
        serializer = PostDetailReviewsSerializer(reviews, many=True)
        return Response(serializer.data)


class ActionsListView(APIView):
    """Список акций"""

    def get(self, request):
        actions = Post.objects.filter(public=True, is_action=True)
        serializer = PostSerializer(actions, many=True)
        return Response(serializer.data)


class NewsListView(APIView):
    """Список акций"""

    def get(self, request):
        actions = Post.objects.filter(public=True, is_news=True)
        serializer = PostSerializer(actions, many=True)
        return Response(serializer.data)


class AboutPageView(APIView):
    """Страницы о нас"""

    def get(self, request):
        """Общая информация"""
        response_data = []
        info = About.objects.last()
        info_serializer = AboutPageSerializer(info, many=False)
        response_data.append(info_serializer.data)  # 0 index - Информация для странницы

        photos = PhotoGallery.objects.filter(public_on_about=True)
        photos_serializer = PhotoSanadSerializer(photos, many=True)
        response_data.append(photos_serializer.data)  #1 index - Фотографии

        videos = VideoGallery.objects.filter()
        videos_serializer = VideoSanadSerializer(videos, many=True)
        response_data.append(videos_serializer.data)    #2 index - Видео

        return Response(response_data)
