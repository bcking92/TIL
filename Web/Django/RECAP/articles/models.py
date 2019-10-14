from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-pk',)


    # method도 추가예정

    # url 만들어주는 method
    def get_absolute_url(self):
        # string을 직접 적어주지 않고 장고 내부의 reverse()함수를 통해 return 값을 정해줄 것임
        # reverse('어느 뷰함수로 갈건지', '인자')
        return reverse('articles:detail', kwargs={'article_pk':self.pk})