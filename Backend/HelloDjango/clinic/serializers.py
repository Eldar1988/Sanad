from rest_framework import serializers

from .models import Direction, Healing, Doctor, Action, DoctorReviews, ImageGallery, VideoGallery, \
    Certificate, Appointment, Price

from blog.serializers import PostListSerializer, MedicalStoriesSerializer


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class HealingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Healing
        exclude = ('order', 'direction')


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class VideoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoGallery
        fields = ('id', 'title', 'video', 'avatar')


class ImageGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageGallery
        fields = ('id', 'title', 'source')


class ActionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('title', 'title_2', 'title_3', 'image', 'slug', 'show_on_home_page')


class ActionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'


class DoctorReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorReviews
        fields = ('id', 'avatar', 'video')


class DoctorListSerializer(serializers.ModelSerializer):
    directions = serializers.SlugRelatedField(slug_field='title', read_only=True, many=True)
    doctor_reviews = DoctorReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'avatar', 'directions', 'slug', 'experience', 'specialization', 'doctor_reviews')


class DirectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'title', 'icon', 'slug', 'is_for_kids_direction', 'is_adults_direction')


class PriceSerializer(serializers.ModelSerializer):
    direction = DirectionListSerializer(many=False, read_only=True)
    
    class Meta:
        model = Price
        exclude = ('date', 'update', 'order')


class ForReviewsDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'specialization')


class DoctorReviewsListSerializer(serializers.ModelSerializer):
    doctor = ForReviewsDoctorSerializer(many=False)

    class Meta:
        model = DoctorReviews
        fields = ('id', 'avatar', 'doctor', 'video')


class DirectionDetailSerializer(serializers.ModelSerializer):
    healing = HealingListSerializer(many=True, read_only=True)
    doctors = DoctorListSerializer(many=True)
    actions = ActionListSerializer(many=True)
    posts = PostListSerializer(many=True)
    stories = MedicalStoriesSerializer(many=True)
    images = ImageGallerySerializer(many=True)
    videos = VideoGallerySerializer(many=True)

    class Meta:
        model = Direction
        fields = '__all__'


class DoctorDetailSerializer(serializers.ModelSerializer):
    directions = DirectionListSerializer(many=True, read_only=True)
    actions = ActionListSerializer(many=True, read_only=True)
    posts = PostListSerializer(many=True, read_only=True)
    stories = MedicalStoriesSerializer(many=True, read_only=True)
    doctor_reviews = DoctorReviewsSerializer(many=True, read_only=True)
    images = ImageGallerySerializer(many=True, read_only=True)
    videos = VideoGallerySerializer(many=True, read_only=True)
    certificates = CertificatesSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'
