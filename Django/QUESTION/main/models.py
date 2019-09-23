from django.db import models

class Question(models.Model):
    content = models.TextField()
    answer = models.TextField()
    reference = models.TextField()
    major = models.ForeignKey(Major, on_delete=CASCADE)

class Major(models.Model):
    major = models.TextField()