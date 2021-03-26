from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Doctor, Direction, Action
from .serializers import DoctorListSerializer, DoctorDetailSerializer, DirectionListSerializer, \
    DirectionDetailSerializer, ActionListSerializer, ActionDetailSerializer


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
        serializer = ActionListSerializer(action, many=False)
        return Response(serializer.data)

