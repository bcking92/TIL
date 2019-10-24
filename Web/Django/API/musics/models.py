from django.db import models

class Artist(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Music(models.Model):
    title = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
