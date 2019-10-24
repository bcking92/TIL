from django.db import models
from django.contrib.auth import 


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = 
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.title
