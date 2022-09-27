from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название ресторана')
    description = models.TextField(verbose_name='Описание')
    count_of_employers = models.IntegerField(verbose_name='Количество работников')
    director = models.CharField(max_length=30, verbose_name='Директор')
    chef = models.CharField(max_length=30, verbose_name='Шеф-повар')
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Дом')
    serves_hot_dogs = models.BooleanField(default=False, verbose_name='Сервис хот-догов')
    serves_pizza = models.BooleanField(default=False, verbose_name='Сервис пиццы')
    serves_sushi = models.BooleanField(default=False, verbose_name='Сервис суши')
    serves_burgers = models.BooleanField(default=False, verbose_name='Сервис бургеров')
    serves_donats = models.BooleanField(default=False, verbose_name='Сервис донатов')
    serves_coffee = models.BooleanField(default=False, verbose_name='Сервис кофе')

    def __str__(self):
        return f'{self.name} ({self.city})'

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
        db_table = 'restaurant'


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='Название ресторана')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    sex = models.CharField(max_length=30, verbose_name='Пол')
    country = models.CharField(max_length=30, verbose_name='Страна')
    city = models.CharField(max_length=30, verbose_name='Город')
    street = models.CharField(max_length=30, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Дом')
    apartment = models.IntegerField(verbose_name='Квартира')
    seniority = models.TextField(verbose_name='Должность')
    education = models.TextField(max_length=50, verbose_name='Образование')
    cources = models.TextField(max_length=50, verbose_name='Курсы')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
        db_table = 'waiter'
