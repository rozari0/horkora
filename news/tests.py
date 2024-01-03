from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from news.models import Article


# Create your tests here.
class HomePageTests(TestCase):
    def test_by_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_by_name(self):
        self.assertEqual(self.client.get(reverse("home")).status_code, 200)

    def test_correct_template(self):
        self.assertTemplateUsed(self.client.get(reverse("home")), "news/newslist.html")


class ArticleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="misirali",
            email="misirali@penguins.club",
            password="veryverysecret",
        )
        cls.article = Article.objects.create(
            title="Very Interesting News",
            summery="Summery",
            news_link="https://news.link",
        )

    def test_article_model(self):
        self.assertEqual(self.post.title, "misirali")
