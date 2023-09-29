from django.urls import path
from django.contrib.syndication.views import Feed
from django.urls import reverse
from news.models import News


class LatestNewsFeed(Feed):
    title = "Horkora News Feed"
    link = "/feed/latest/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return News.objects.all()[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summery

    def item_link(self, item):
        return item.news_link


urlpatterns = [
    path("latest/", LatestNewsFeed()),
]
