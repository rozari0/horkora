"""
URL configuration for horkora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from news.views import (
    about,
    addNews,
    categories,
    editNews,
    index,
    index_page,
    single_category,
    viewnews,
)

from .api import api_v1

urlpatterns = [
    path("", index),
    path("categories/", categories, name="Categories"),
    path("categories/<str:category>", single_category, name="Categories"),
    path("<int:page>/", index_page, name="Pagination"),
    path("addnews/", addNews),
    path("news/<int:newsid>", viewnews),
    path("about/", about, name="About"),
    path("editnews/<int:newsid>/", editNews),
    path("api_v1/", api_v1.urls),
    path("feed/", include("news.feed")),
]
