from django.urls import path
from App_Login import views

app_name = "App_Login"


urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_page, name='login'),
  path('edit/', views.edit_profile, name='edit'),
  path('profile/',views.profile, name='profile'),
  path('logout/', views.user_logout, name='logout'),
  path('user/<username>/', views.user, name='user'),
  path('follow/<username>/', views.follow, name='follow'),
  path('unfollow/<username>/', views.unfollow, name='unfollow'),
    ]