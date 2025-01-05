from django.urls import path
from library.apps import LibraryConfig
from library.views import BooksListApiView, BooksRetrieveApiView, BooksCreateApiView, BooksDestroyApiView, \
    BooksUpdateApiView, AuthorListApiView, AuthorRetrieveApiView, AuthorDestroyApiView, AuthorCreateApiView, \
    AuthorUpdateApiView

app_name = LibraryConfig.name


urlpatterns = [
    path('books/', BooksListApiView.as_view(), name='books_list'),
    path('books/<int:pk>/', BooksRetrieveApiView.as_view(), name='books_retrieve'),
    path('books/create/', BooksCreateApiView.as_view(), name='books_create'),
    path('books/<int:pk>/delete/', BooksDestroyApiView.as_view(), name='books_delete'),
    path('books/<int:pk>/update/', BooksUpdateApiView.as_view(), name='books_update'),
    path('author/', AuthorListApiView.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorRetrieveApiView.as_view(), name='author_retrieve'),
    path('author/create/', AuthorCreateApiView.as_view(), name='author_create'),
    path('author/<int:pk>/delete/', AuthorDestroyApiView.as_view(), name='author_delete'),
    path('author/<int:pk>/update/', AuthorUpdateApiView.as_view(), name='author_update'),
]

