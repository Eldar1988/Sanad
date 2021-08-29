from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import MainInfo, Slider, Advantage, Contacts, About, VideoGallery, PhotoGallery, Banner, InfoPage
from .serializers import MainInfoSerializer, SliderSerializer, ContactsSerializer, \
    AboutPageSerializer, VideoSanadSerializer, PhotoSanadSerializer, BannerSerializer, InfoPageListSerializer, \
    InfoPageDetailSerializer


class MainInfoView(APIView):
    """Основная информация для сайта"""

    def get(self, request):
        response_data = {}

        meta = MainInfo.objects.last()
        meta_serializer = MainInfoSerializer(meta, many=False)
        response_data['meta'] = meta_serializer.data

        slides = Slider.objects.filter(public=True)
        slides_serializer = SliderSerializer(slides, many=True)
        response_data['slides'] = slides_serializer.data

        contacts = Contacts.objects.last()
        contacts_serializer = ContactsSerializer(contacts, many=False)
        response_data['contacts'] = contacts_serializer.data

        return Response(response_data)


class AboutSanadView(APIView):
    """Информация о клинике"""

    def get(self, request):
        info = About.objects.last()
        serializer = AboutPageSerializer(info, many=False)
        return Response(serializer.data)


class VideoGalleryView(generics.ListAPIView):
    """Видеогалерея"""
    queryset = VideoGallery.objects.all()
    serializer_class = VideoSanadSerializer


class PhotoGalleryView(generics.ListAPIView):
    """Фотогалерея"""
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoSanadSerializer


class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.filter(public=True)
    serializer_class = BannerSerializer


class InfoPageListView(generics.ListAPIView):
    queryset = InfoPage.objects.filter(public=True)
    serializer_class = InfoPageListSerializer


class InfoPageDetailView(generics.RetrieveAPIView):
    queryset = InfoPage.objects.filter(public=True)
    serializer_class = InfoPageDetailSerializer
    lookup_field = 'slug'
