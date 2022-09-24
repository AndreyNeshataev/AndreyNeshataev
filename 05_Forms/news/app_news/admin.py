from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'article', 'created_date', 'updated_date', 'activity_flag')
    list_editable = ('activity_flag',)
    # prepopulated_fields = {"slug": ("title",)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'created_date', 'commentary', 'news')
    list_editable = ('user_name', 'commentary')
    search_fields = ('name',)
