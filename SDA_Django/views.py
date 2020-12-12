from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect

from django.views.generic.base import TemplateView


class HomeView(TemplateView):

    template_name = "home.html"
    extra_context = {"title": "Home"}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("login")