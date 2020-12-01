from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class PostListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = "posts"
    ordering = ["-date_posted"]
    extra_context = {"title": "Blog"}
    paginate_by = 5

    def get_queryset(self):
        category_name = self.kwargs['category']
        posts = Post.objects.filter(category__name=category_name)
        return posts