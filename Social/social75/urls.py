from django.urls import path
from . import views

urlpatterns = [
    path('habits/', views.habit_list, name='habit_list'),  # List all habits
    path('habits/<int:pk>/', views.habit_detail, name='habit_detail'),  # Detail of a specific habit
]
