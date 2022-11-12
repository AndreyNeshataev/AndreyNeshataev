from django.contrib import admin
from app_library.models import Book, Author


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Класс Администратор Книги"""
    list_display = ('id', 'author_book', 'title', 'isbn', 'year_of_release', 'number_of_pages')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Класс Администратор Автор"""
    list_display = ('id', 'name', 'surname', 'date_of_birth')
