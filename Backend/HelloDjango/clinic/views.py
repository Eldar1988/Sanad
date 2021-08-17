from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Doctor, Direction, Action, DoctorReviews, Appointment
from .serializers import DoctorListSerializer, DoctorDetailSerializer, DirectionListSerializer, \
    DirectionDetailSerializer, ActionListSerializer, ActionDetailSerializer, DoctorReviewsListSerializer, \
    DoctorReviewsSerializer, AppointmentSerializer

from .service import send_tg_message


class CreateAppointmentView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_tg_message(instance)


class DoctorsListView(generics.ListAPIView):
    queryset = Doctor.objects.filter(public=True)
    serializer_class = DoctorListSerializer


class DoctorDetailView(APIView):
    def get(self, request, slug):
        doctor = Doctor.objects.get(slug=slug)
        serializer = DoctorDetailSerializer(doctor, many=False)
        return Response(serializer.data)


class DirectionsListView(generics.ListAPIView):
    queryset = Direction.objects.all()
    serializer_class = DirectionListSerializer


class DirectionDetailView(APIView):
    def get(self, request, slug):
        direction = Direction.objects.get(slug=slug)
        serializer = DirectionDetailSerializer(direction, many=False)
        return Response(serializer.data)


class ActionsListView(generics.ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionListSerializer


class ActionDetailView(APIView):
    def get(self, request, slug):
        action = Action.objects.get(slug=slug)
        serializer = ActionDetailSerializer(action, many=False)
        return Response(serializer.data)


class HomePageReviewsListView(generics.ListAPIView):
    """Отзывы о врачах для главной страницы"""
    queryset = DoctorReviews.objects.filter(public_on_home_page=True, public=True)
    serializer_class = DoctorReviewsListSerializer


class ReviewsListView(generics.ListAPIView):
    """Все отзывы о врачах"""
    queryset = DoctorReviews.objects.filter(public=True)
    serializer_class = DoctorReviewsListSerializer


class ReviewDetailView(APIView):
    """Отзыв детали"""

    def get(self, request, pk):
        review = DoctorReviews.objects.get(id=pk)
        serializer = DoctorReviewsSerializer()
        return Response(serializer.data)
