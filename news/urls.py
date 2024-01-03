from django.urls import include, path
from django.views.generic import TemplateView

from news.views import (
    CategoriesList,
    DetailNews,
    NewsList,
    about,
    addNews,
    editNews,
    single_category,
)

from .api import api_v1

urlpatterns = [
    path("", NewsList.as_view(), name="home"),
    path("news/", NewsList.as_view(), name="news_list"),
    path("news/<int:page>/", NewsList.as_view(), name="news_list_page"),
    path("categories/", CategoriesList.as_view(), name="categories"),
    path("categories/<slug:slug>", single_category, name="categories_to"),
    path("addnews/", addNews, name="write"),
    path("article/<int:pk>/", DetailNews.as_view(), name="article"),
    path("about/", about, name="about"),
    path("editnews/<int:newsid>/", editNews),
    path("api_v1/", api_v1.urls),
    path("feed/", include("news.feed")),
    path("theme/",TemplateView.as_view(template_name='news/theme.html'),name="theme"),
]
