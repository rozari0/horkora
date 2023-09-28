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
            "is_draft",
        )
