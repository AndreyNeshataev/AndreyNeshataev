from django.db import models
from django.utils.translation import gettext_lazy as _


class Marketplace(models.Model):
    name_shop = models.CharField(max_length=100, verbose_name=_('Название магазина'))
    sale_date = models.DateField(auto_now=False, verbose_name=_('Дата установления скидки'))

    def __str__(self):
        return self.name_shop or ''

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')
        ordering = ['name_shop', ]


class Goods(models.Model):
    name_goods = models.CharField(max_length=100, verbose_name=_('Название товара'))
    description = models.TextField(max_length=1000, blank=True, verbose_name=_('Описание товара'))

    def __str__(self):
        return self.name_goods

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ['name_goods', ]


class Variation(models.Model):
    product = models.ForeignKey('Goods', on_delete=models.CASCADE, related_name="variations", verbose_name=_("Товар"))
    quantity = models.PositiveIntegerField(default=0,  verbose_name=_("Количество товара"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Цена товара'))
    sale = models.IntegerField(default=0, verbose_name=_('Скидка в процентах'))
    shop = models.ForeignKey('Marketplace', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Магазин"))

    def __str__(self):
        return self.product.name_goods

    def get_price(self):
        self.price = round(float(self.price) - (float(self.price) * float(self.sale / 100)), 2)
        return self.price

    class Meta:
        verbose_name = _('Вариация')
        verbose_name_plural = _('Вариации')

