from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.CharField(max_length=300)
    # 데이터가 들어간 순간을 찍어라
    created_at = models.DateTimeField(auto_now_add=True)
    # 그냥 실행된 순간을 찍어라(이렇게하면 업데이트된 시간을 추적할 수 있음)
    updated_at = models.DateTimeField(auto_now=True)
    
    