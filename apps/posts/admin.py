from django.contrib import admin
from django.db import models
from markdownx.widgets import AdminMarkdownxWidget

from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_select_related = ("category",)
    list_display = ("title", "published", "category")

    fields = (
        "title",
        "content",
        "thumbnail",
        "slug",
        "description",
        "category",
        "status",
        "is_page",
        "published",
        "updated",
        "created",
    )

    readonly_fields = ("updated", "created")
    formfield_overrides = {models.TextField: {"widget": AdminMarkdownxWidget}}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")
    fields = ("name", "slug", "order")


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
