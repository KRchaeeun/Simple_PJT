from django.urls import path
from . import views

urlpatterns = [
    # 1. 날씨 API 테스트 - 서울의 5일 치 예보 데이터 확인 
    path("", views.index),  
    # 2. 예보 데이터 중 원하는 데이터만 DB에 저장  
    path("save-data/", views.save_data),  # RESTful
    # 3. 저장된 데이터 전체 조회  
    path("list-data", views.list_data),
    # 4. 특정 조건 데이터 확인: 섭씨 30도가 넘는 시간대 조회
    path("hot-weathers/", views.hot_weathers)
]
