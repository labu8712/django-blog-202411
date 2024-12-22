from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from blog.filters import PostFilter
from blog.forms import CategoryForm, CommentForm, PostForm
from blog.models import Category, Post
from core.forms import DeleteConfirmForm


def post_list(request):
    post_filter = PostFilter(
        request.GET or None,
        queryset=Post.objects.select_related("category").prefetch_related("tags"),
    )
    return render(request, "blog/post_list.html", {"post_filter": post_filter})


@login_required
@permission_required("blog.add_post", raise_exception=True)
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
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


@login_required
@permission_required("blog.change_post", raise_exception=True)
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Post update success.")
        return redirect("blog:post-detail", pk=pk)

    return render(request, "blog/post_update.html", {"form": form})


@login_required
@permission_required("blog.delete_post", raise_exception=True)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        post.delete()
        messages.success(request, "刪除成功")
        return redirect("blog:post-list")

    return render(request, "blog/post_delete.html", {"form": form, "post": post})


@login_required
def post_create_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

        messages.success(request, "留言成功")

    return redirect("blog:post-detail", pk=post_pk)


@login_required
@permission_required("blog.view_category", raise_exception=True)
def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
        "blog/category_list.html",
        {"categories": categories},
    )


@login_required
@permission_required("blog.add_category", raise_exception=True)
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Category create success.")
        return redirect("blog:category-list")

    return render(request, "blog/category_create.html", {"form": form})


@login_required
@permission_required("blog.view_category", raise_exception=True)
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, "blog/category_detail.html", {"category": category})


@login_required
@permission_required("blog.change_category", raise_exception=True)
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        messages.success(request, "Category update success.")
        return redirect("blog:category-detail", pk=pk)

    return render(request, "blog/category_update.html", {"form": form})


@login_required
@permission_required("blog.delete_category", raise_exception=True)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    form = DeleteConfirmForm(request.POST or None)
    if form.is_valid():
        category.delete()
        messages.success(request, "刪除成功")
        return redirect("blog:category-list")

    return render(
        request,
        "blog/category_delete.html",
        {"form": form, "category": category},
    )
