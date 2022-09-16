from django.urls import reverse
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, db_index=True, verbose_name='Заголовок')
    description = models.CharField(max_length=1500, default='', verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    price_RUB = models.FloatField(verbose_name='цена_RUB', default=0)
    price_USD = models.FloatField(verbose_name='цена_USD', default=0, null=True)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True,
                               on_delete=models.PROTECT, related_name='advertisements',
                               verbose_name='Статус')
    type = models.ForeignKey('AdvertisementType', default=None, null=True,
                             on_delete=models.PROTECT, related_name='advertisements',
                             verbose_name='Тип')
    author = models.ForeignKey('AdvertisementAuthor', default=None, null=True,
                               on_delete=models.CASCADE, related_name='advertisements',
                               verbose_name='Автор')
    cat = models.ForeignKey('AdvertisementCategory', default=None, null=True,
                            on_delete=models.PROTECT, related_name='advertisements',
                            verbose_name='Категории')

    def __str__(self):
        return self.title

    def counter(self):
        self.views_count += 1
        return self.views_count

    # def get_absolute_url(self):
    #     return reverse('advertisement-detail', kwargs={'advertisement_id': self.pk})

    class Meta:
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'
        db_table = 'advertisements'
        ordering = ['created_date', 'title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, verbose_name='Статус объявления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100, default=None, null=True, verbose_name='Тип объявления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Тип'


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Имя')
    mail = models.EmailField(max_length=100, default=None, null=True, verbose_name='Email')
    phoneNumber = models.CharField(max_length=12, default=None, null=True, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
