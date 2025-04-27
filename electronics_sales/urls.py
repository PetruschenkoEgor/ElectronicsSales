from django.urls import path

from electronics_sales.apps import ElectronicsSalesConfig
from electronics_sales.serializers import SalesNetworkSerializer
from electronics_sales.views import SalesNetworkCreate, SalesNetworkUpdate, SalesNetworkList, SalesNetworkRetrieve, \
    SalesNetworkDestroy

app_name = ElectronicsSalesConfig.name

urlpatterns = [
    path('sales-network-create/', SalesNetworkCreate.as_view(serializer_class=SalesNetworkSerializer), name='sales-network-create'),
    path('<int:pk>/sales-network-update/', SalesNetworkUpdate.as_view(serializer_class=SalesNetworkSerializer), name='sales-network-update'),
    path('sales-networks/', SalesNetworkList.as_view(serializer_class=SalesNetworkSerializer), name='sales-networks'),
    path('<int:pk>/info-sales-network/', SalesNetworkRetrieve.as_view(serializer_class=SalesNetworkSerializer), name='info-sales-network'),
    path('<int:pk>/destroy-sales-network/', SalesNetworkDestroy.as_view(serializer_class=SalesNetworkSerializer), name='destroy-sales-network'),
]
