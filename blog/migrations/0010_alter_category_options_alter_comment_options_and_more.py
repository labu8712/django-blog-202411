# Generated by Django 5.1.3 on 2024-12-22 02:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_post_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "soft_delete",
                )
            },
        ),
        migrations.AlterModelOptions(
            name="comment",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "soft_delete",
                )
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"permissions": [("change_post_status", "Can change post status")]},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "soft_delete",
                )
            },
        ),
        migrations.AddField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="category",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="comment",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="post",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tag",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="tag",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
