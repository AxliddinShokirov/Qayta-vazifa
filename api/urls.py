from django.urls import path
from api import views

urlpatterns = [
    path('banner_list/', views.Banner_list),
    path('banner_detail/<int:pk>/', views.Banner_detail),
    path('category_list/', views.Category_list),
    path('category_detail/<int:pk>/', views.Category_detail),
    path('gym_list/', views.Gym_list),
    path('gym_detail/<int:pk>/', views.Gym_detail),
    path('coach_list/', views.Coach_list),
]