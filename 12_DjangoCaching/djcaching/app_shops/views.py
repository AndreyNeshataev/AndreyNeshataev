from django.shortcuts import render, redirect
from app_shops.models import Shop, Offers
from django.contrib.auth.models import User
from app_shops.models import Goods
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse
from app_users.models import PurchaseHistory
from django.core.cache import cache
import random
import datetime
from django.utils.translation import gettext_lazy as _


def home_page(request, *args, **kwargs):
    user_cache = cache.get_many(['offers', 'shops'])
    goods = Goods.objects.all()
    if not user_cache:
        offers = Offers.objects.all()
        shops = Shop.objects.all()
        user_cache = {
            'offers': offers,
            'shops': shops,
        }
        cache.set_many(user_cache, 60 * 5)
    context = user_cache
    context['goods'] = goods
    return render(request, 'shops/home.html', context=context)


def shops_list(request, *args, **kwargs):
    shops = cache.get_or_set('shops', Shop.objects.all(), 60 * 5)
    return render(request, 'shops/shops_list.html', {'shops': shops})


class ShopPage(ListView):
    model = Shop
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        shop = Shop.objects.get(id=kwargs['pk'])
        goods_list = Goods.objects.filter(shop_id=shop.id)
        days = [_("Понедельник"), _("Вторник"), _("Среда"), _("Четверг"), _("Пятница"), _("Суббота"), _("Воскресенье")]
        day_number = datetime.date.today().weekday()
        day = days[day_number]
        right_day = False
        if day_number in [4, 5, 6]:
            right_day = True
        if shop.sale_date != datetime.date.today():
            for goods in goods_list:
                if day_number in [5, 6]:
                    goods.sale = random.randrange(2, 30, 5)
                elif day_number == 4:
                    goods.sale = random.randrange(2, 10, 2)
                else:
                    goods.sale = 0
                goods.save()
                shop.sale_date = datetime.date.today()
                shop.save()
        return render(request, 'shops/shop_page.html', {'shop': shop,
                                                        'goods_list': goods_list,
                                                        'day': day,
                                                        'right_day': right_day})

    def post(self, request, *args, **kwargs):
        if 'goods_id' in request.POST:
            goods_id = request.POST.get('goods_id')
            goods = Goods.objects.get(id=goods_id)
            sale_price = goods.get_price()
            user = request.user
            if goods.price <= user.profile.balance:
                PurchaseHistory.objects.create(user=user, goods=goods, price=sale_price)
                user.profile.balance = float(user.profile.balance) - float(sale_price)
                user.profile.save()
            else:
                return HttpResponse(_("Недостаточно средств, пополните баланс"))
        return redirect('home')
