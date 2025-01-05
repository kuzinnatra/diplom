from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from library.models import Books, Author
from library.pagination import BooksPaginator, AuthorPaginator
from users.permissions import IsLibrarian
from library.serializer import BooksSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend


"""Контроллеры для книг"""
class BooksCreateApiView(CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsLibrarian]


class BooksListApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = BooksPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'name', 'user', 'availability', 'author']


class BooksRetrieveApiView(RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BooksUpdateApiView(UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsLibrarian]


class BooksDestroyApiView(DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsLibrarian]


"""Контроллеры для Авторов"""
class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian,]


class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]


class AuthorRetrieveApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian]


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsLibrarian]
