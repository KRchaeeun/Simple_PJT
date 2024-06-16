from django.urls import path
from movies import views


urlpatterns = [
    path('movies/', views.movie_list),                              # 전체 영화 목록 제공
    path('movies/<int:movie_pk>/', views.movie_detail),             # 단일 영화 정보 제공(출연배우 이름과 리뷰 목록 포함)
    path('actors/', views.actor_list),
    path('actors/<int:actor_pk>/', views.actor_detail),
    path('reviews/', views.review_list),                            # 전체 리뷰 목록 제공
    path('reviews/<int:reviews_pk>/', views.review_detail),         # 단일 리뷰 조회 & 수정 & 삭제
    path('movies/<int:movie_pk>/reviews', views.review_create),     # 리뷰 생성
]
