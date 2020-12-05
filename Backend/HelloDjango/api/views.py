from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from sanad.models import MainInfo
from .serializers import MainInfoSerializer


class HomePageView(APIView):
    """Информация для Header и Head"""

    def get(self, request):
        response_data = []

        # Логотип, title, description
        info = MainInfo.objects.last()
        info_serializer = MainInfoSerializer(info, many=False)
        response_data.append(info_serializer.data)  # 0 index - Логотип, title, description

        return Response(response_data)


