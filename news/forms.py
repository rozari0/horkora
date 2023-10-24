from django import forms

from news.models import Article


class NewsForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "author",
            "summery",
            "news_link",
            "archive_link",
            "category",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "u-full-width"}),
            "news_link": forms.URLInput(attrs={"class": "u-full-width"}),
            "summery": forms.Textarea(attrs={"class": "u-full-width"}),
        }
