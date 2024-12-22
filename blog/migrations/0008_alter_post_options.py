# Generated by Django 5.1.3 on 2024-12-22 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_post_options_alter_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "soft_delete",
                ),
                "permissions": [
                    ("publish_post", "Can publish post"),
                    ("change_post_status", "Can change post status"),
                ],
            },
        ),
    ]