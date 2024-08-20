from django.urls import path
from api import views

urlpatterns = [
     path('Banner/', views.BannerView.as_view()),
    path('Banner/<int:id>/', views.BannerView.as_view()),
    path('Coach/view/', views.CoachView.as_view()),
    path('Coach/view/<int:id>/', views.CoachView.as_view()),
    path('Info/view/', views.InfoView.as_view()),
    path('Info/view/<int:id>/', views.InfoView.as_view()),
    path('Product/view/', views.ProductView.as_view()),
    path('Product/view/<int:id>', views.ProductView.as_view()),
    path('Category/view/', views.CategoryView.as_view()),
    path('Category/view/<int:id>/', views.CategoryView.as_view()),
    path('Gym/view/', views.GymView.as_view()),
    path('Gym/view/<int:id>/', views.GymView.as_view()),
    path('Reja/view/', views.RejaView.as_view()),
    path('Reja/view/<int:id>/', views.RejaView.as_view()),
]