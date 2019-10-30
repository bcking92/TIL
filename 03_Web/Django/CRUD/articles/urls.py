from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.new),
    path('create/', views.create),
    path('post/<int:num>/', views.post),
]