from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from electronics_sales.models import Product, SalesNetwork
from electronics_sales.serializers import ProductSerializer, SalesNetworkSerializer
from users.permissions import IsActiveUser


class SalesNetworkCreate(generics.CreateAPIView):
    """Создание звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SalesNetworkUpdate(generics.UpdateAPIView):
    """Редактирование звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SalesNetworkFilterCountry(filters.FilterSet):
    """Фильтрация по стране."""

    country = filters.CharFilter(field_name="contacts__country", lookup_expr="iexact")

    class Meta:
        model = SalesNetwork
        fields = ["country"]


class SalesNetworkList(generics.ListAPIView):
    """Список звеньев сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SalesNetworkFilterCountry
    permission_classes = [IsAuthenticated, IsActiveUser]


class SalesNetworkRetrieve(generics.RetrieveAPIView):
    """Информация о звене сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class SalesNetworkDestroy(generics.DestroyAPIView):
    """Удаление звена сети продажи электроники."""

    queryset = SalesNetwork.objects.all()
    serializer_class = SalesNetworkSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductCreate(generics.CreateAPIView):
    """Создание продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductUpdate(generics.UpdateAPIView):
    """Редактирование продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductList(generics.ListAPIView):
    """Список продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductRetrieve(generics.RetrieveAPIView):
    """Информация о продукте."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]


class ProductDestroy(generics.DestroyAPIView):
    """Удаление продукта."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActiveUser]
