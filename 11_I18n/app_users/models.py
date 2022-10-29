from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    city = models.CharField(max_length=36, blank=True, verbose_name=_("Город"))
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_("Дата рождения"))
    number_phone = models.CharField(max_length=12, blank=True, verbose_name=_("Номер телефона"))
    about_me = models.TextField(max_length=500, blank=True, null=True, verbose_name=_("Обо мне"))
    avatar = models.FileField(upload_to="avatar/%Y/%m/%d/", null=True, blank=True, verbose_name=_("Аватар"))

    class Meta:
        verbose_name = _('Информация о пользователях')
        verbose_name_plural = _('Информация о пользователях')
        ordering = ['user']
