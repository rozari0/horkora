from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, View

from news.forms import NewsForm
from news.models import About, Category, Article


# Create your views here.
class NewsList(View):
    def get(self, request, page=1):
        news = Article.objects.all()
        paginator = Paginator(news, 3)
        page = paginator.get_page(page)
        return render(
            request,
            "news/newslist.html",
            context={
                "articles": page,
                "page": {
                    "current": page.number,
                    "has_next": page.has_next(),
                    "has_previous": page.has_previous(),
                    "next": page.number + 1,
                    "previous": page.number - 1,
                },
            },
        )


class DetailNews(DetailView):
    model = Article
    template_name = "news/viewnews.html"
    context_object_name = "news"


class CategoriesList(ListView):
    model = Category
    template_name = "news/categories.html"
    context_object_name = "categories"


def single_category(request, slug):
    article = Article.objects.filter(category=get_object_or_404(Category, slug=slug))
    print(article)
    return render(
        request,
        template_name="news/category.html",
        context={"articles": article, "category": slug.capitalize()},
    )


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
            form = form.save()
            return redirect("article", pk=form.id)
    form = NewsForm()
    return render(request, template_name="news/addnews.html", context={"form": form})


@permission_required("news.edit_news", raise_exception=True, login_url="/admin/")
def editNews(request, newsid):
    newsinfo = Article.objects.get(pk=newsid)
    form = NewsForm(instance=newsinfo)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=newsinfo)
        if form.is_valid():
            form.save()
            return redirect("news", pk=newsid)
    return render(request, template_name="news/addnews.html", context={"form": form})


@permission_required("news.delete_news", raise_exception=True, login_url="/admin/")
def deleteNews(request):
    return render(request, template_name="news/index.html")
