from django.urls import path
from app_library.views import BookList, BookDetail, AuthorList, AuthorDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='books_list'),
    path('<int:pk>/book_detail/', BookDetail.as_view(), name='book_detail'),
    path('author/', AuthorList.as_view(), name='author_list'),
    path('<int:pk>/author_detail/', AuthorDetail.as_view(), name='author_detail'),
]