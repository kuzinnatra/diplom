from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='автор книги')

class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name='название книги')
    availability = models.BooleanField(verbose_name='наличие книги')
    genre = models.CharField(max_length=100, verbose_name='жанр книги')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='пользователь', **NULLABLE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
