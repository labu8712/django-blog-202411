from django.shortcuts import render

from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_create(request):
    return render(request, "blog/post_create.html")
