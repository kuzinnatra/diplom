from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='почта',
        unique=True
    )
    phone = models.CharField(max_length=55, verbose_name='телефон', **NULLABLE)
    name = models.CharField(max_length=100, verbose_name='ФИО пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
