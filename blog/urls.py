from django.urls import path
from blog.views import PostListView

urlpatterns = [
    path('blog/<str:category>', PostListView.as_view(), name='post-list'),
]
