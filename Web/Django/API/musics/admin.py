from django.contrib import admin
from .models import Comment, Artist, Music

# Register your models here.
admin.site.register(Comment)
admin.site.register(Artist)
admin.site.register(Music)
