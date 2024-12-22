import os
import uuid

from django.db import models
from django.urls import reverse
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True
        default_permissions = ("add", "change", "delete", "view", "soft_delete")


def post_image_path(instance, filename):
    new_filename = f"{uuid.uuid4()}{os.path.splitext(filename)[1]}"
    now = timezone.now()
    return f"post_image/{now:%Y/%m/%d}/{new_filename}"


class Category(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("blog:tag-detail", kwargs={"pk": self.pk})


class Post(BaseModel):
    class Status(models.TextChoices):
        PUBLIC = "public", "Public"
        PRIVATE = "private", "Private"

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(
        max_length=7,
        choices=Status,
        default=Status.PUBLIC,
    )
    image = models.ImageField(blank=True, null=True, upload_to=post_image_path)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="posts",
    )
    tags = models.ManyToManyField(Tag, related_name="posts")

    class Meta:
        permissions = [
            # ("publish_post", "Can publish post"),
            ("change_post_status", "Can change post status"),
        ]

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    nick_name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    def __str__(self) -> str:
        return self.content
