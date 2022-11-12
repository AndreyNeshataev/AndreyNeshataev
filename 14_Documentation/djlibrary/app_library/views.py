from app_library.models import Book, Author
from app_library.serializers import BookSerializer, AuthorSerializer
from rest_framework import generics


class BookList(generics.ListCreateAPIView):
    """
    Класс - представление для получения списка Книг и создания новых Книг
    """
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Функция для формирования списка Книг, по заданным параметрам
        """
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        title = self.request.query_params.get('title')
        number_of_pages = self.request.query_params.get('number_of_pages')
        if author and title:
            author_id = Author.objects.get(name=author).id
            queryset = queryset.filter(title=title).filter(author_book_id=author_id)
        if number_of_pages:
            queryset = queryset.filter(number_of_pages__lte=number_of_pages)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        Функция для получения списка Книг по запросу пользователя.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Функция для создания новой записи Книга в базу данных.
        """
        return self.create(request, *args, **kwargs)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс - представление для получения детальной информации о Книге,
    а также для редактирования и удаления информации.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        """
        Функция для получения необходимой Книги по запросу пользователя.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Функция для изменения информации по Книге по запросу пользователя.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Функция для удаления выбранной Книги.
        """
        return self.destroy(request, *args, **kwargs)


class AuthorList(generics.ListCreateAPIView):
    """
    Класс - представление для получения списка Авторов и добавления новых Авторов
    """
    serializer_class = AuthorSerializer

    def get_queryset(self):
        """
        Функция для формирования списка Авторов, по заданным параметрам
        """
        queryset = Author.objects.all()
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name=name)
        return queryset

    def get(self, request, *args, **kwargs):
        """
        Функция для получения списка Авторов по запросу пользователя.
        """
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Функция для создания новой записи Книга в базу данных.
        """
        return self.create(request, *args, **kwargs)


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Класс - представление для получения детальной информации об Авторе,
    а также для редактирования и удаления информации.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        """
        Функция для получения информации об Авторе.
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """
        Функция для изменения информации об Авторе.
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Функция для удаления информации об Авторе.
        """
        return self.destroy(request, *args, **kwargs)
