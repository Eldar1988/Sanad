from rest_framework import serializers

from sanad.models import MainInfo, Slider, Contacts
from clinic.models import Direction, Doctor, Healing, DirectionReviews, DoctorReviews, Action, Certificate, \
    VideoGallery, ImageGallery

from blog.models import MedicalHistory, Post
from blog.serializers import PostReviewListSerializer, PostSerializer


class MainInfoSerializer(serializers.ModelSerializer):
    """Информация для заголовков"""

    class Meta:
        model = MainInfo
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):
    """Акции"""

    class Meta:
        model = Action
        exclude = ('update', 'pub_date', 'description', 'doctors', 'directions')


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


class VideoGallerySerializer(serializers.ModelSerializer):
    """Видео врачей"""

    class Meta:
        model = VideoGallery
        exclude = ('pub_date', 'update', 'order', 'doctors', 'directions')


class ImageGallerySerializer(serializers.ModelSerializer):
    """Видео врачей"""

    class Meta:
        model = ImageGallery
        exclude = ('pub_date', 'update', 'order', 'doctors', 'directions')


class DoctorReviewsSerializer(serializers.ModelSerializer):
    """Отзывы к доктору"""

    class Meta:
        model = DoctorReviews
        exclude = ('update', 'pub_date', 'public_on_home_page')


class MedicalHistorySerializer(serializers.ModelSerializer):
    """Истории болезни"""

    class Meta:
        model = MedicalHistory
        exclude = ('pub_date', 'update', 'doctor', 'direction', 'order', 'body')


class DoctorCertificateSerializer(serializers.ModelSerializer):
    """Сертификаты доктора"""

    class Meta:
        model = Certificate
        fields = '__all__'


class DoctorsDetailSerializer(serializers.ModelSerializer):
    """ Список докторов"""
    reviews = DoctorReviewsSerializer(many=True)
    actions = ActionSerializer(many=True)
    certificates = DoctorCertificateSerializer(many=True)
    stories = MedicalHistorySerializer(many=True)
    videos = VideoGallerySerializer(many=True)
    images = ImageGallerySerializer(many=True)
    posts = PostSerializer(many=True)

    class Meta:
        model = Doctor
        exclude = ('pub_date', 'views', 'update', 'public', 'order', 'direction')


class HealingSerializer(serializers.ModelSerializer):
    """Этапы лечения"""

    class Meta:
        model = Healing
        exclude = ('order',)


class DirectionReviewsSerializer(serializers.ModelSerializer):
    """Отзывы к направлениям"""

    class Meta:
        model = DirectionReviews
        exclude = ('pub_date', 'update', 'public', 'public_on_home_page')


class ContactsSerializer(serializers.ModelSerializer):
    """Контактная информация"""

    class Meta:
        model = Contacts
        fields = '__all__'

