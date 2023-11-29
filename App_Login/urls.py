from django.urls import path
from App_Login import views


urlpatterns = [
  path('signup/', views.signup, name='signup'),
    ]