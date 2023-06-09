# Generated by Django 4.2 on 2023-04-26 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0004_article_dislike"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("likeapp", "0002_likerecord_delete_like"),
    ]

    operations = [
        migrations.CreateModel(
            name="DisLikeRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dis_like_record",
                        to="articleapp.article",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dis_like_record",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"unique_together": {("user", "article")},},
        ),
    ]
