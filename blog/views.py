from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post
from blog.forms import PostForm


class PostListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = "posts"
    extra_context = {"title": "Blog"}
    paginate_by = 3

    def get_queryset(self):
        category_name = self.kwargs['category']
        posts = Post.objects.filter(category__name=category_name).order_by('-date_posted')
        return posts


class PostDetailView(DetailView):

    template_name = "blog/post.html"
    model = Post
    slug_url_kwarg = 'slug'


class PostCreateView(CreateView):

    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("home")

