# Generated by Django 5.1.3 on 2024-12-15 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_category_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="posts/image/%Y/%m/%d/"
            ),
        ),
    ]
