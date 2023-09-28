# Generated by Django 4.2.4 on 2023-09-25 18:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_news_author_alter_news_category_alter_news_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="published_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="news",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
