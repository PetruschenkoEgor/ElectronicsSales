from rest_framework import generics

from users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """Регистрация пользователя."""

    serializer_class = UserSerializer
