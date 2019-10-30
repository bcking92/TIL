from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # blank=True <- not null을 허용하는것 
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Meta 클래스를 이용해 Post클래스에 속성을 부여하자
    # Meta에 대해 더 궁금하면 django document에서 meta option을 확인하자
    # 이건 DB가 바뀌는게아니고 ORM수준에서 처리하는것 그러므로 migrate 할 필요 없이 적용됨.
    class Meta:
        # '-pk' == pk의 반대순서로 순서를 매겨라!
        ordering = ['-pk']
    # user = ForeignKey

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # on_delete=참조하는 테이블이 사라졌을 때 데이터를 어떻게 할지 묻는것
    # on_delete=models.CASCADE <- (폭포수처럼)다 지우겠다
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']

    # user = ForeignKey

    # models.OneToOne()
    # modles.ManyToMany()

# class User(models.Model):
#     name = 
#     password =
#     address =
#     email = 
    