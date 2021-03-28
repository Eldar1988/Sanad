from django.urls import path
from . import views


urlpatterns = [
    path('home_page_posts/', views.HomePagePostsListView.as_view()),
    path('posts/', views.PostsListView.as_view()),
    path('actual_posts/', views.ActualPostsListView.as_view()),
    path('clinic_life_posts/', views.ClinicLifePostsView.as_view()),
    path('post/<slug:slug>/', views.PostDetailView.as_view()),
    path('home_page_medical_stories/', views.HomePageMedicalStoriesView.as_view()),
    path('medical_stories/', views.MedicalStoriesView.as_view()),
    path('medical_story/<slug:slug>/', views.MedicalStoryDetailView.as_view())
]
