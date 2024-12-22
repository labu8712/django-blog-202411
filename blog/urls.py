from django.urls import path
from django.views.generic import CreateView

from blog import views as blog_views
from blog.models import Tag

app_name = "blog"

urlpatterns = [
    path("posts/", blog_views.post_list, name="post-list"),
    path("posts/create/", blog_views.post_create, name="post-create"),
    path("posts/<int:pk>/", blog_views.post_detail, name="post-detail"),
    path("posts/<int:pk>/update/", blog_views.post_update, name="post-update"),
    path("posts/<int:pk>/delete/", blog_views.post_delete, name="post-delete"),
    path(
        "posts/<int:post_pk>/comment/",
        blog_views.post_create_comment,
        name="post-create-comment",
    ),
    path("categories/", blog_views.category_list, name="category-list"),
    path("categories/create/", blog_views.category_create, name="category-create"),
    path("categories/<int:pk>/", blog_views.category_detail, name="category-detail"),
    path(
        "categories/<int:pk>/update/",
        blog_views.category_update,
        name="category-update",
    ),
    path(
        "categories/<int:pk>/delete/",
        blog_views.category_delete,
        name="category-delete",
    ),
    path("tags/", blog_views.TagListView.as_view(), name="tag-list"),
    path("tags/create/", blog_views.TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/", blog_views.TagDetailView.as_view(), name="tag-detail"),
    path(
        "tags/<int:pk>/update/",
        blog_views.TagUpdateView.as_view(),
        name="tag-update",
    ),
]
