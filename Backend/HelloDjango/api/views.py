from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from sanad.models import MainInfo, Slider
from clinic.models import Direction, Doctor, Healing, DirectionReviews
from blog.models import MedicalHistory

from .serializers import MainInfoSerializer, SliderSerializer, DirectionListSerializer, DirectionDetailSerializer, \
    DoctorsListSerializer, HealingSerializer, DirectionReviewsSerializer, MedicalHistorySerializer


class HomePageView(APIView):
    """Информация для главной страницы"""

    def get(self, request):
        response_data = []

        # Логотип, title, description
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
        direction_serializer = DirectionDetailSerializer(direction, many=False)
        response_data.append(direction_serializer.data)  # 0 index - Инормация о направлении

        # Специалисты направления
        doctors = Doctor.objects.filter(public=True, direction__slug=slug)
        doctors_serializer = DoctorsListSerializer(doctors, many=True)
        response_data.append(doctors_serializer.data)  # 1 index - Специалисты направления

        # Этапы лечения
        healing = Healing.objects.filter(direction__slug=slug)
        healing_serializer = HealingSerializer(healing, many=True)
        response_data.append(healing_serializer.data)   # 2 index - этапы лечения

        # Отзывы
        reviews = DirectionReviews.objects.filter(public=True, direction__slug=slug)
        reviews_serializer = DirectionReviewsSerializer(reviews, many=True)
        response_data.append(reviews_serializer.data)   # 3 index - отзывы

        # Истории болезни
        stories = MedicalHistory.objects.filter(public=True, direction__slug=slug)
        stories_serializer = MedicalHistorySerializer(stories, many=True)
        response_data.append(stories_serializer.data)   # 4 index - Истории болезни

        return Response(response_data)
