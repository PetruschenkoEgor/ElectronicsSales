from rest_framework import generics
from django_filters import rest_framework as filters
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


class SalesNetworkFilterCountry(filters.FilterSet):
    """Фильтрация по стране."""

    country = filters.CharFilter(field_name='contacts__country', lookup_expr='iexact')

    class Meta:
        model = SalesNetwork
        fields = ['country']


class SalesNetworkList(generics.ListAPIView):
    """Список звеньев сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SalesNetworkFilterCountry


class SalesNetworkRetrieve(generics.RetrieveAPIView):
    """Информация о звене сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer


class SalesNetworkDestroy(generics.DestroyAPIView):
    """Удаление звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
