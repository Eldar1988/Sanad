from rest_framework import serializers

from sanad.models import MainInfo, Slider
from clinic.models import Direction, Doctor, Healing, DirectionReviews
from blog.models import MedicalHistory


class MainInfoSerializer(serializers.ModelSerializer):
    """Информация для Heder"""

    class Meta:
        model = MainInfo
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    """Слайдер"""

    class Meta:
        model = Slider
        exclude = ('order', 'pub_date', 'update', 'public')


class DirectionListSerializer(serializers.ModelSerializer):
    """Список направлений"""

    class Meta:
        model = Direction
        fields = ('id', 'title', 'icon', 'short_description', 'slug')


class DirectionDetailSerializer(serializers.ModelSerializer):
    """Список направлений"""

    class Meta:
        model = Direction
        exclude = ('pub_date', 'order', 'update', 'views')


class DoctorsListSerializer(serializers.ModelSerializer):
    """ Список докторов"""

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'avatar', 'short_description', 'slug')


class HealingSerializer(serializers.ModelSerializer):
    """Этапы лечения"""

    class Meta:
        model = Healing
        exclude = ('order',)


class DirectionReviewsSerializer(serializers.ModelSerializer):
    """Отзывы к направлениям"""

    class Meta:
        model = DirectionReviews
        exclude = ('pub_date', 'update', 'public', 'order', 'public_on_home_page')


class MedicalHistorySerializer(serializers.ModelSerializer):
    """Истории болезни"""

    class Meta:
        model = MedicalHistory
        exclude = ('pub_date', 'update', 'views', 'doctor', 'direction', 'order')
