from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('blog/<str:category>', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
]
