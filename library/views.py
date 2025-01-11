from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

from library.models import Book, Author
from library.pagination import BookPaginator, AuthorPaginator
from users.permissions import IsLibrarian
from library.serializer import BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend


"""Контроллеры для книг"""
class BookCreateApiView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarian]


class BookListApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPaginator
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'name', 'user', 'availability', 'author']


class BookRetrieveApiView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsLibrarian]

    def perform_update(self, serializer):
        if serializer.validated_data.get('user'):
            is_available = False
        else:
            is_available = True
        serializer.save(availability=is_available)


class BookDestroyApiView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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
