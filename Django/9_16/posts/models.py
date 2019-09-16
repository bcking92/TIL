from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    # on_delete=참조하는 테이블이 사라졌을 때 데이터를 어떻게 할지 묻는것
    # on_delete=models.CASCADE <- (폭포수처럼)다 지우겠다
    # models.OneToOne()
    # modles.ManyToMany()