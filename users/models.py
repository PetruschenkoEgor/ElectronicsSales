from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(max_length=150, unique=True, verbose_name='Ник')
    email = models.EmailField(unique=True, verbose_name='Email')
    name = models.CharField(max_length=150, verbose_name='Имя', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Активный сотрудник')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
