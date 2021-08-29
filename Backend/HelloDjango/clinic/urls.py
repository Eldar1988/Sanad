from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.DoctorsListView.as_view()),
    path('doctor/<slug:slug>/', views.DoctorDetailView.as_view()),
    path('directions/', views.DirectionsListView.as_view()),
    path('direction/<slug:slug>/', views.DirectionDetailView.as_view()),
    path('actions/', views.ActionsListView.as_view()),
    path('actions/<slug:slug>/', views.ActionDetailView.as_view()),
    path('home_reviews/', views.HomePageReviewsListView.as_view()),
    path('reviews/', views.ReviewsListView.as_view()),
    path('review/<int:pk>/', views.ReviewDetailView.as_view()),
    path('create_appointment/', views.CreateAppointmentView.as_view()),
    path('price/', views.PriceView.as_view())
]