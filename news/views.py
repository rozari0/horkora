from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from news.models import Category, News, About
from news.forms import NewsForm

# Create your views here.


def index_page(request, page):
    context = {}
    news = News.objects.all()
    paginator = Paginator(news, per_page=5)
    context["articles"] = paginator.get_page(page)
    return render(request=request, template_name="news/index.html", context=context)


def index(request):
    context = {}
    news = News.objects.all().order_by("id")
    paginator = Paginator(news, per_page=5)
    context["articles"] = paginator.get_page(1)
    return render(request=request, template_name="news/index.html", context=context)


def viewnews(request, newsid):
    news = get_object_or_404(News, pk=newsid)
    return render(request, template_name="news/viewnews.html", context={"news": news})


def about(request):
    return render(
        request,
        template_name="news/about.html",
        context={"about": About.objects.first()},
    )


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
            return viewnews(request, newsid)
    return render(request, template_name="news/addnews.html", context={"form": form})


@permission_required("news.delete_news", raise_exception=True, login_url="/admin/")
def deleteNews(request):
    return render(request, template_name="news/index.html")
