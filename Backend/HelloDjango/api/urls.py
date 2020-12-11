from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view()),   # Главная страница
    path('direction/<slug:slug>', views.DirectionDetailView.as_view()),    # Страница направления
    path('doctor/<slug:slug>', views.DoctorDetailView.as_view()),   # Странца доктора
    path('contacts/', views.ContactsView.as_view()),    # Контакная информация

    path('post/<slug:slug>', views.PostDetailView.as_view()),    # Детали поста
    path('post_reviews/<slug:slug>', views.PostDetailReviewsView.as_view()),    # Отзывы к посту
    path('actions/', views.ActionsListView.as_view()),   # Страница акций
    path('news/', views.NewsListView.as_view()),    # Страница новостей
    path('about/', views.AboutPageView.as_view())   # Страница новостей
]
