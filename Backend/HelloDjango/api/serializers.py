from rest_framework import serializers

from sanad.models import MainInfo


class MainInfoSerializer(serializers.ModelSerializer):
    """Информация для Heder"""

    class Meta:
        model = MainInfo
        fields = '__all__'
