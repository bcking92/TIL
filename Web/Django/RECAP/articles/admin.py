from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # admin에서 볼 정보들을 튜플형태로 
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')
    # admin 화면에서 데이터 link를 설정해줌
    list_display_links = ('title',)
    
admin.site.register(Article, ArticleAdmin)