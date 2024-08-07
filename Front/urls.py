from django.urls import path , include

from . import views

urlpatterns = [
    path('', views.front, name='index'),
    path('', include('Front.login.urls'), name='login'),
    path('coach', views.coach, name='coach')
    ]