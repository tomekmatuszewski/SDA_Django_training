from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('blog/<str:category>', PostListView.as_view(), name='post-list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('blog/post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/update', PostUpdateView.as_view(), name='post-update'),
    path('blog/<slug:slug>/delete', PostDeleteView.as_view(), name='post-delete'),
]
