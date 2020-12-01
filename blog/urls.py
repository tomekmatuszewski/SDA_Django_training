from django.urls import path
from blog.views import view

urlpatterns = [
    path('blog/', view, name='post-list'),
]
