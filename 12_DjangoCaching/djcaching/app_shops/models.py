from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Shop(models.Model):
    name_shop = models.CharField(max_length=100, verbose_name=_('Название магазина'))
    sale_date = models.DateField(auto_now=False, verbose_name=_('Дата установления скидки'))

    def __str__(self):
        return self.name_shop

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')
        ordering = ['name_shop', ]


class Goods(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='shop_goods', verbose_name=_('Магазин'))
    name_goods = models.CharField(max_length=100, verbose_name=_('Название товара'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена товара'))
    sale = models.IntegerField(verbose_name=_('Скидка в процентах'), blank=True, default=0)

    def __str__(self):
        return self.name_goods

    def get_price(self):
        self.price = round(float(self.price) - (float(self.price) * float(self.sale / 100)), 2)
        return self.price

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['name_goods', ]


class Offers(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, null=True, blank=True,
                             related_name='shop_offers', verbose_name=_('Магазин'))
    offer = models.CharField(max_length=500, verbose_name=_('Предложение магазина'))

    class Meta:
        verbose_name = _('Предложение магазина')
        verbose_name_plural = _('Предложения магазина')


