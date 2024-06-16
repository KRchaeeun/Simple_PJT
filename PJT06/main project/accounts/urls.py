from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
  path('login/', views.login, name='login'),
  path('logout/', views.logout, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('delete/', views.delete, name='delete'),
  path('update/', views.update, name='update'),
  path('password/', views.change_password, name='change_password'),
  path('<username>/', views.profile, name='profile'),
  path('<int:user_pk>/follow/', views.follow, name='follow'),
  path('<username>/followers/', views.follower_list, name='follower_list'),
  path('<username>/followings/', views.following_list, name='following_list'),
  path('<username>/likemovies/', views.like_movies_list, name='like_movies_list'),
]
