from django import forms

from news.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
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
