"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 패키지 처럼 새로 불러옴
from pages import views


urlpatterns = [
    # root의 주소는 빈스트링으로 표현
    path('', views.index),
    # path()
    # 첫번째 인자 : 주문서(url경로)
    # 두번째 인자 : view 함수의 위치
    path('admin/', admin.site.urls),
    # trailing comma 를 붙이는 것이 장고의 관례임 
    # path('index/', pages.index),
    path('index/', views.index),
    path('home/', views.home),
    path('lotto/', views.lotto),

    # interactive한 페이지 만들기
    path('cube/<int:num>', views.cube),
    path('match/', views.match),

    # 새로운 앱
    # artii로 시작하는 url이 나오면 artii.urls.py가 처리하도록 해라! include는 import 해야함.
    path('artii/', include('artii.urls')),
]
