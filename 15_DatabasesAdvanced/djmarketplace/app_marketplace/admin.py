from django.contrib import admin
from .models import *


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_shop', 'sale_date')
    list_editable = ('name_shop', 'sale_date')


class Variationline(admin.TabularInline):
    model = Variation


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_goods', 'description', )
    inlines = [Variationline, ]
