from django.shortcuts import render, redirect
from app_marketplace.models import Marketplace, Goods, Variation
from django.views.generic import ListView
from django.urls import reverse_lazy
from app_users.models import PurchaseHistory
from django.core.cache import cache
from datetime import timedelta, date
from django.utils.translation import gettext_lazy as _
from app_marketplace.utils import sale
from cart.cart import Cart
from django.db.models import Sum, F, Max
from sentry_sdk import capture_message


class HomePage(ListView):
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        if not (cache.get('day') and cache.get('right_day')):
            right_day, day = sale(**kwargs)
            day_cache = {'right_day': right_day,
                         'day': day}
            cache.set_many(day_cache, timeout=60 * 60)
        capture_message('Все норм')
        goods = Goods.objects.only('id', 'name_goods').all().order_by('name_goods')
        vars = Variation.objects.select_related('product', 'shop').all()
        aggregate = {}
        if request.user.is_authenticated:
            var_list = list(map(lambda x: (x.product, x.shop, x.get_price()), vars))
        else:
            var_list = list(map(lambda x: (x.product, x.shop, x.price), vars))
        for good in goods:
            var = list(filter(lambda x: x[0].id == good.id, var_list))
            aggregate[good.name_goods] = [good.id, var]
        return render(request, 'shops/home.html', {'aggregate': aggregate,
                                                   'cart': cart})


def shops_list(request, *args, **kwargs):
    cart = Cart(request)
    shops = cache.get_or_set('shops', Marketplace.objects.all(), 60 * 5)
    return render(request, 'shops/shops_list.html', {'shops': shops,
                                                     'cart': cart})


class ShopPage(ListView):
    model = Marketplace
    # success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        cart = Cart(request)
        shop = Marketplace.objects.get(id=kwargs['pk'])
        if 'pk_2' in kwargs:
            variation_list = Variation.objects.filter(shop_id=kwargs['pk'],
                                                      product_id=kwargs['pk_2']).select_related('product', 'shop')
        else:
            variation_list = Variation.objects.filter(shop_id=kwargs['pk']).select_related('product', 'shop')

        return render(request, 'shops/shop_page.html', {'shop': shop,
                                                        'variation_list': variation_list,
                                                        'day': cache.get('day'),
                                                        'right_day': cache.get('right_day'),
                                                        'cart': cart})


def report_on_best_selling(request, *args, **kwargs):
    max_items = []
    pk = kwargs['pk']
    period = ''
    if pk == 1:
        max_items = PurchaseHistory.objects.filter(
            purchase_date__gte=date.today()).values('goods').annotate(
            added_field=F("goods__name_goods"),
            quantity_sum=Sum('quantity')).order_by('-quantity_sum')[:3]
        period = _('сегодня')
    elif pk == 2:
        week = date.today() - timedelta(minutes=60 * 24 * 7)
        print(date.today())
        max_items = PurchaseHistory.objects.filter(
            purchase_date__gte=week).values('goods').annotate(
            added_field=F("goods__name_goods"),
            quantity_sum=Sum('quantity')).order_by('-quantity_sum')[:3]
        period = _('неделю')
    elif pk == 3:
        month = date.today() - timedelta(minutes=60 * 24 * 30)
        max_items = PurchaseHistory.objects.filter(
            purchase_date__gte=month).values('goods').annotate(
            added_field=F("goods__name_goods"),
            quantity_sum=Sum('quantity')).order_by('-quantity_sum')[:3]
        period = _('месяц')
    elif pk == 4:
        max_items = PurchaseHistory.objects.values('goods').annotate(
            added_field=F("goods__name_goods"),
            quantity_sum=Sum('quantity')).order_by('-quantity_sum')[:3]
        period = _('за всё время')

    return render(request, 'shops/report.html', context={'max_items': max_items,
                                                         'header': _('Отчет за {}').format(period)})
