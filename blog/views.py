from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'blog/blog.html'
    context_object_name = "posts"
    extra_context = {"title": "Blog"}
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category']
        posts = Post.objects.filter(category__name__contains=category_name).order_by('-date_posted')
        return posts


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "blog/post.html"
    model = Post
    slug_url_kwarg = 'slug'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(
            reverse_lazy("post-list", kwargs={'category': form.cleaned_data['category']}))


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("post-list", kwargs={"category": self.object.category})

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
