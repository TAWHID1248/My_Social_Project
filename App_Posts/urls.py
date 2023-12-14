from django.urls import path
from App_Posts import views

app_name = 'App_Posts'


urlpatterns = [
    path('', views.home, name='home'),
    path('like/<pk>/', views.liked, name='liked'),
    path('unlike/<pk>/', views.unliked, name='unliked'),
]

