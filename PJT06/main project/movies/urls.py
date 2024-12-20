from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:pk>/', views.detail, name='detail'),
  path('create/', views.create, name='create'),
  path('<int:pk>/delete/', views.delete, name='delete'),
  path('<int:pk>/update/', views.update, name='update'),
  path('<int:movie_pk>/comments/', views.comments_create, name='comments_create'),
  path('<int:movie_pk>/comments/<int:parent_comment_id>/', views.comments_create, name='comments_create_with_parent'),
  path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
  path('<int:movie_pk>/likes/', views.likes, name='likes'),
]
