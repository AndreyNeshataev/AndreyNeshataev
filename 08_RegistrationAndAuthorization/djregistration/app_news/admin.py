from django.contrib import admin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import *


# Register your models here.
class CommentsInline(admin.TabularInline):
    model = Comments


@admin.register(News)
class NewsAdmin(PermissionRequiredMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date', 'activity_flag', 'published', 'slug')
    list_filter = ('created_date', 'tags')
    inlines = [CommentsInline]
    prepopulated_fields = {"slug": ("title",)}
    actions = ['mark_as_active', 'mark_as_inactive', 'mark_as_published', 'mark_as_not_published']

    # list_editable = ('activity_flag',)

    def mark_as_active(self, request, obj):
        obj.update(activity_flag='a')

    def mark_as_inactive(self, request, obj):
        obj.update(activity_flag='i')

    def mark_as_published(self, request, obj):
        obj.update(published=True)

    def mark_as_not_published(self, request, obj):
        obj.update(published=False)

    mark_as_active.short_description = "Перевести в статус Активно"
    mark_as_inactive.short_description = "Перевести в статус Неактивно"
    mark_as_published.short_description = "Перевести в статус Опубликовано"
    mark_as_not_published.short_description = "Перевести в статус Не опубликовано"


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'created_date', 'get_commentary', 'news')
    search_fields = ('user_name',)
    list_filter = ('user_name',)

    actions = ['mark_as_delete', 'mark_as_undesirable']

    # list_editable = ('user_name', 'commentary')

    def get_commentary(self, obj):
        if len(obj.commentary) > 25:
            return obj.commentary[:25] + '...'
        return obj.commentary

    def mark_as_delete(self, request, obj):
        obj.update(commentary='Удалено администратором')

    def mark_as_undesirable(self, request, obj):
        obj.update(commentary='Данный комментарий не удовлетворяет условиям политики сайта')

    get_commentary.short_description = "Комментарии"
    mark_as_delete.short_description = "Удалить"
    mark_as_undesirable.short_description = "Нежелательное"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {"slug": ("title",)}