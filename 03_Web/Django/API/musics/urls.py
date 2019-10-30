from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

app_name = 'musics'

schema_view = get_schema_view(
    openapi.Info(
        title='Music API',
        default_version='v1',
    )
)

urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:music_id>/', views.music_detail, name='music_detail'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('musics/<int:music_id>/comments/', views.comments_create, name='comments_create'),

    path('docs/', schema_view.with_ui('redoc'), name='api_docs'),
    path('swagger/', schema_view.with_ui('swagger'), name='api_swagger'),
    
]