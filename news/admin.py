from django.contrib import admin
from django.db import models

from .models import About, Category, News

# Register your models here.
admin.site.register(News)
admin.site.register(Category)
admin.site.register(About)
