from django.shortcuts import render


def view(request):
    return render(request, 'blog/blog.html')


