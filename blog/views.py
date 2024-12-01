from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from blog.forms import CommentForm, PostForm
from blog.models import Post
from core.forms import DeleteConfirmForm


def post_list(request):
    posts = Post.objects.select_related("category").prefetch_related("tags")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Post create success.")
        return redirect("blog:post-list")

    return render(request, "blog/post_create.html", {"form": form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comment_form": comment_form},
    )


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Post update success.")
        return redirect("blog:post-detail", pk=pk)

    return render(request, "blog/post_update.html", {"form": form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, "刪除成功")
        return redirect("blog:post-list")

    return render(request, "blog/post_delete.html", {"form": form, "post": post})


def post_create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        messages.success(request, "留言成功")

    return redirect("blog:post-detail", pk=post_pk)
