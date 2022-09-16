from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price_RUB', 'status', 'type', 'cat', 'author')
    list_editable = ('price_RUB', 'status', 'type', 'cat')


@admin.register(AdvertisementAuthor)
class AdvertisementAuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'phoneNumber')
    list_editable = ('mail', 'phoneNumber')


@admin.register(AdvertisementStatus)
class AdvertisementStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(AdvertisementType)
class AdvertisementTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)


@admin.register(AdvertisementCategory)
class AdvertisementCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)

