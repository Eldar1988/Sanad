from rest_framework.views import APIView
from rest_framework import generics

from .models import Doctor
from .serializers import DoctorListSerializer, DoctorDetailSerializer


class DoctorsListView(generics.ListAPIView):
    queryset = Doctor.objects.filter(public=True)
    serializer_class = DoctorListSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = 