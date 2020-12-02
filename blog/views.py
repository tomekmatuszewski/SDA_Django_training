from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
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


class PostDetailView(DetailView):

    template_name = "blog/post.html"
    model = Post
    slug_url_kwarg = 'slug'

