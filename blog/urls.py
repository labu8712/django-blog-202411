from django.urls import path

from blog import views as blog_views

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
]
