from django.urls import include, path
from . import views


urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('banner/', views.bannercrud, name='bannercrud'),
    path('listbanner/', views.listBanner, name='listbanner'),
    path('createbanner/', views.createBanner, name='createbanner'),
    path('deletebanner/<int:id>/', views.deleteBanner, name='delete'),
    path('category/', views.listCategory, name='category_list'),
    path('createcategory/', views.createCategory, name='create_category'),
    path('deletecategory/<int:id>/', views.deleteCategory, name='delete_category'),
     path('create', views.createGym, name='createGym'),
    path('list', views.listGym, name='listGym'),
    path('detail/<int:id>/', views.detailProduct, name='detailGym'),
    path('delete/<int:id>/', views.deleteGym, name='deleteGym'),
    path('blog_name/', views.Blog_name, name='blogName'),


]