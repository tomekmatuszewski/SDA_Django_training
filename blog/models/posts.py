from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from blog.utils import change_pic_size


class Category(models.Model):
    name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='posts')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=20)
    image = models.ImageField(upload_to="blog_pics", default="default.png", help_text="Min. size 525x1024")

    def __str__(self):
        return f"Post {self.id}, title: {self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        change_pic_size(self.image.path, 525, 1024)

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})
