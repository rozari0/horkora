from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import About, Category, News


# TinyMCE
class textEditorAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


# Register your models here.
admin.site.register(News, textEditorAdmin)
admin.site.register(Category)
admin.site.register(About, textEditorAdmin)
