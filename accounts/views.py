from django.shortcuts import render, redirect
from accounts.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are able to log in."
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})


class LoginViewOwn(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("home")
