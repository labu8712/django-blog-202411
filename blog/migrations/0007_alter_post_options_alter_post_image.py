# Generated by Django 5.1.3 on 2024-12-22 01:56

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_post_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={
                "permissions": [
                    ("publish_post", "Can publish post"),
                    ("change_post_status", "Can change post status"),
                ]
            },
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=blog.models.post_image_path
            ),
        ),
    ]