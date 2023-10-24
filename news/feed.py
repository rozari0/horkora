from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django.urls import path, reverse

from news.models import Category, Article


class LatestNewsFeed(Feed):
    title = "Horkora News Feed"
    link = "/feed/latest/"
    description = "Horkokra News Feed in Rss Format."

    def items(self):
        return Article.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summery

    def item_link(self, item):
        return item.news_link


class LatestNewsFeedCategory(Feed):
    def get_object(self, request, category):
        return get_object_or_404(Category, slug=category)

    def title(self, obj):
        return "News in %s" % obj.title

    def link(self, obj):
        return ""

    def description(self, obj):
        return "Recent news in %s" % obj.title

    def items(self, obj):
        return Article.objects.filter(category=obj)[:30]


urlpatterns = [
    path("latest/", LatestNewsFeed()),
    path("<str:category>/", LatestNewsFeedCategory()),
]
