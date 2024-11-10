from django.contrib import messages
from django.shortcuts import redirect, render

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Post create success.")
        return redirect("blog:post-list")

    return render(request, "blog/post_create.html", {"form": form})
