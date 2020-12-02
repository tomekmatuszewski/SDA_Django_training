from django.urls import path
from blog.views import PostListView, PostDetailView

urlpatterns = [
    path('blog/<str:category>', PostListView.as_view(), name='post-list'),
    path('blog/post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
]
