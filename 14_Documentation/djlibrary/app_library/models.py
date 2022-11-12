from django.db import models


# Create your models here.
class Author(models.Model):
    """
    Модель Автор, для создания экземпляра класса в базе данных
    """
    name = models.CharField(max_length=20, verbose_name="Имя")
    surname = models.CharField(max_length=30, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="День рождения")

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    """
    Модель Книга, для создания экземпляра класса в базе данных
    """
    author_book = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=200, verbose_name='Название книги')
    isbn = models.CharField(max_length=13, verbose_name='ISBN')
    year_of_release = models.FloatField(verbose_name="Год выпуска")
    number_of_pages = models.IntegerField(verbose_name="Количество страниц")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
