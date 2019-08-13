from django.urls import path
# 현재 폴더에서 views 를 불러라!
from . import views
urlpatterns = [
    # artii/ 로 한벌 걸렀기 때문에 artii 페이지는 ''로 표현함.
    path('', views.artii),
    path('result/', views.result),
]