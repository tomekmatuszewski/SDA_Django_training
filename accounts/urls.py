from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import register, LoginViewOwn

urlpatterns = [
    path("register/", register, name="register"),
    path(
        "login/",
        LoginViewOwn.as_view(),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="accounts/logout.html"),
        name="logout",
    ),
]
