from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('update/<int:article_pk>/', views.update, name='update'),
    path('delete/<int:article_pk>/', views.delete, name='delete'),
    path('<int:article_pk>/comments/', views.comments, name='comments'),
    path('<int:article_pk>/comments_delete/<int:comment_pk>/', views.comments_delete, name='comments_delete'),
]