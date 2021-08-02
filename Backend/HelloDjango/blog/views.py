from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Post, MedicalHistory
from .serializers import PostListSerializer, PostDetailSerializer, MedicalStoriesSerializer, \
    MedicalHistoryDetailSerializer


class HomePagePostsListView(generics.ListAPIView):
    queryset = Post.objects.filter(public_on_home_page=True, public=True, clinic_life=False)[:6]
    serializer_class = PostListSerializer


class PostsListView(generics.ListAPIView):
    queryset = Post.objects.filter(public=True, clinic_life=False)
    serializer_class = PostListSerializer


class ClinicLifePostsView(generics.ListAPIView):
    queryset = Post.objects.filter(public=True, clinic_life=True)
    serializer_class = PostListSerializer


class PostDetailView(APIView):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post.views += 1
        post.save()
        serializer = PostDetailSerializer(post, many=False)
        return Response(serializer.data)


class HomePageMedicalStoriesView(generics.ListAPIView):
    queryset = MedicalHistory.objects.filter(public=True, public_on_home_page=True)[:10]
    serializer_class = MedicalStoriesSerializer


class MedicalStoriesView(generics.ListAPIView):
    queryset = MedicalHistory.objects.filter(public=True)
    serializer_class = MedicalStoriesSerializer


class MedicalStoryDetailView(APIView):
    def get(self, request, slug):
        story = MedicalHistory.objects.get(slug=slug)
        story.views += 1
        story.save()
        serializer = MedicalHistoryDetailSerializer(story, many=False)
        return Response(serializer.data)



