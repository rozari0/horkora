# Generated by Django 4.2.4 on 2023-09-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="is_draft",
            field=models.BooleanField(default=True, verbose_name="This is a draft?"),
        ),
    ]
