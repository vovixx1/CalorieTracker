from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal_list, name='meal_list'),
    path('add/', views.add_meal, name='add_meal'),
    path('delete/<int:meal_id>/', views.delete_meal, name='delete_meal'),
    path('daily_summary/', views.daily_summary, name='daily_summary'),  # Add this line
]
