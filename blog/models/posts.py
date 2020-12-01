from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.id}, title: {self.title}"