from django.urls import path
from App_Login import views

app_name = "App_Login"


urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_page, name='login'),
  path('edit/', views.edit_profile, name='edit'),
  path('logout/', views.user_logout, name='logout'),
    ]