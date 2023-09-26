from django.shortcuts import render
from news.models import News, Category
from django.core.paginator import Paginator

# Create your views here.


def index_page(request, page):
    context = {}
    news = News.objects.all()
    category = Category.objects.all()
    paginator = Paginator(news, per_page=5)
    context["articles"] = paginator.get_page(page)
    context["category"] = category
    return render(request=request, template_name="news/index.html", context=context)


def index(request):
    context = {}
    news = News.objects.all()
    category = Category.objects.all()
    paginator = Paginator(news, per_page=5)
    context["articles"] = paginator.get_page(1)
    context["category"] = category
    return render(request=request, template_name="news/index.html", context=context)
