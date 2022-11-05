from django.contrib import admin
from .models import *


class Goodsline(admin.TabularInline):
    model = Goods


class Offersline(admin.TabularInline):
    model = Offers


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_shop', 'sale_date')
    list_editable = ('name_shop', 'sale_date')
    inlines = [Goodsline, Offersline]


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'name_goods', 'price', 'sale')


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop', 'offer')
