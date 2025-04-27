from rest_framework import generics

from electronics_sales.models import SalesNetwork
from electronics_sales.serializers import SalesNetworkSerializer


class SalesNetworkCreate(generics.CreateAPIView):
    """Создание звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkUpdate(generics.UpdateAPIView):
    """Редактирование звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkList(generics.ListAPIView):
    """Список звеньев сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkRetrieve(generics.RetrieveAPIView):
    """Информация о звене сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkDestroy(generics.DestroyAPIView):
    """Удаление звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
