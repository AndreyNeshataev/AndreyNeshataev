from django.db import models
from django.contrib.auth.models import User
from app_shops.models import Goods
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    city = models.CharField(max_length=36, blank=True, verbose_name=_("Город"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Дата рождения"))
    number_phone = models.CharField(max_length=12, blank=True, verbose_name=_("Номер телефона"))
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name=_('Баланс на счету'))

    class Meta:
        verbose_name = _('Информация о пользователях')
        verbose_name_plural = _('Информация о пользователях')
        ordering = ['user']


class PurchaseHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Пользователь'))
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name=_('Товар'))
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_('Цена товара'))
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата покупки'))

    class Meta:
        verbose_name = _('История покупок')
        verbose_name_plural = _('История покупок')
        ordering = ['-purchase_date', ]
