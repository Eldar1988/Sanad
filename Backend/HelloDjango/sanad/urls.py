from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.AboutSanadView.as_view()),
    path('videos/', views.VideoGalleryView.as_view()),
    path('photos/', views.PhotoGalleryView.as_view()),
    path('banners/', views.BannerListView.as_view()),
    path('', views.MainInfoView.as_view())
]
