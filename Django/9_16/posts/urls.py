from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create, name='create'),
    path('detail/<int:num>/', views.detail, name='detail'),
    path('update/<int:num>/', views.update, name='update'),
    path('delete/<int:num>/', views.delete, name='delete'),
    path('comment/<int:num>/', views.create_comment, name='comment'),
    path('comment/delete/<int:num>/', views.delete_comment, name='delete_comment'),
    path('comment/update/<int:num>/', views.update_comment, name='update_comment'),
]