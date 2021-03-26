from django.urls import path
from . import views

urlpatterns = [
    path('doctors/', views.DoctorsListView.as_view()),
    path('doctor/<slug:slug>/', views.DoctorDetailView.as_view()),
    path('directions/', views.DirectionsListView.as_view()),
    path('direction/<slug:slug>/', views.DirectionDetailView.as_view()),
    path('actions/', views.ActionsListView.as_view()),
    path('actions/<slug:slug>/', views.ActionDetailView.as_view())
]