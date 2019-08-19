from django.db import models

# Create your models here.
class Article(models.Model):
    # 자료의 타입을 Text 라고 말해줌
    title = models.TextField()
    content = models.TextField()
    # 자료의 타입이 DateTime 이라고 해주고, 
    created_at = models.DateTimeField(auto_now_add=True)
    img_url = models.TextField()

    def __str__(self):
        return f'{self.id} {self.title}'


class StudentModel(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    age = models.IntegerField()
	
    def __str__(self):
        return f'{self.name}'