from django.contrib import admin
from django.db import models

from .models import About, Category, Article

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(About)
