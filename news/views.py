from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from news.models import Category, News
from news.forms import NewsForm

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


@permission_required("news.add_news", raise_exception=True, login_url="/admin/")
def addNews(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    form = NewsForm()
    return render(request, template_name="news/addnews.html", context={"form": form})


@permission_required("news.edit_news", raise_exception=True, login_url="/admin/")
def editNews(request, newsid):
    newsinfo = News.objects.get(pk=newsid)
    form = NewsForm(instance=newsinfo)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=newsinfo)
        if form.is_valid():
            form.save(commit=True)
    return render(request, template_name="news/addnews.html", context={"form": form})


@permission_required("news.delete_news", raise_exception=True, login_url="/admin/")
def deleteNews(request):
    return render(request, template_name="news/index.html")
