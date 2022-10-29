from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date', 'published', 'slug')  #'published_date',
    list_filter = ('created_date', 'tags')
    prepopulated_fields = {"slug": ("title",)}
    actions = ['mark_as_published', 'mark_as_not_published']

    def mark_as_published(self, request, obj):
        obj.update(published=True)

    def mark_as_not_published(self, request, obj):
        obj.update(published=False)

    mark_as_published.short_description = _("Перевести в статус Опубликовано")
    mark_as_not_published.short_description = _("Перевести в статус Не опубликовано")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'photo')

