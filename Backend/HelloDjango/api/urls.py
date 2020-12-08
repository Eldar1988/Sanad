from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),   # Главная страница
    path('direction/<slug>', views.DirectionDetailView.as_view())    # Страница направления
]