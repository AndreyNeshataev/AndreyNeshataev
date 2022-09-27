from django.contrib import admin
from .models import *


# Register your models here.
class CommentsInline(admin.TabularInline):
    model = Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_date', 'activity_flag')
    list_filter = ('activity_flag',)
    inlines = [CommentsInline]

    actions = ['mark_as_active', 'mark_as_inactive']

    # list_editable = ('activity_flag',)
    # prepopulated_fields = {"slug": ("title",)}

    def mark_as_active(self, request, obj):
        obj.update(activity_flag='a')

    def mark_as_inactive(self, request, obj):
        obj.update(activity_flag='i')

    mark_as_active.short_description = "Перевести в статус Активно"
    mark_as_inactive.short_description = "Перевести в статус Неактивно"


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'created_date', 'get_commentary', 'news')
    search_fields = ('user_name',)
    list_filter = ('user_name',)

    actions = ['mark_as_delete', 'mark_as_undesirable']

    # list_editable = ('user_name', 'commentary')

    def get_commentary(self, obj):
        return obj.commentary[:25]

    def mark_as_delete(self, request, obj):
        obj.update(commentary='Удалено администратором')

    def mark_as_undesirable(self, request, obj):
        obj.update(commentary='Нежелательное')

    get_commentary.short_description = "Комментарии"
    mark_as_delete.short_description = "Удалить"
    mark_as_undesirable.short_description = "Нежелательное"
