# Generated by Django 4.2 on 2023-04-26 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("articleapp", "0005_article_when"),
    ]

    operations = [
        migrations.RemoveField(model_name="article", name="when",),
    ]