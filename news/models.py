from django.db import models
from django.db.models.signals import pre_save

from utils.scrape import scrape_summery


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name="News Title", max_length=250, blank=True)
    author = models.CharField(
        verbose_name="News Author", max_length=100, blank=True, null=True
    )
    summery = models.TextField(verbose_name="Summery Of the News", blank=True)
    news_link = models.URLField(verbose_name="News Link")
    archive_link = models.URLField(verbose_name="Archive Link of News", blank=True)
    category = models.ManyToManyField("Category", blank=True)
    is_draft = models.BooleanField(verbose_name="This is a draft.", default=True)
    published_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.title != "":
            return self.title
        return "Die"


def news_pre_save(sender, instance, *args, **kwargs):
    data = scrape_summery(instance.news_link)
    if instance.title == "":
        instance.title = data.get("title")
    if instance.summery == "":
        instance.summery = data.get("summery")
    if instance.author == "":
        instance.author = data.get("author")


class Category(models.Model):
    title = models.CharField(verbose_name="Categories of News", max_length=50)

    def __str__(self):
        return self.title


pre_save.connect(news_pre_save, sender=News)
