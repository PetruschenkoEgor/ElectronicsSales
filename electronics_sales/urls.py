from django.urls import path

from electronics_sales.apps import ElectronicsSalesConfig
from electronics_sales.views import SalesNetworkCreate, SalesNetworkUpdate, SalesNetworkList, SalesNetworkRetrieve, \
    SalesNetworkDestroy

app_name = ElectronicsSalesConfig.name

urlpatterns = [
    path('sales-network-create/', SalesNetworkCreate.as_view(), name='sales-network-create'),
    path('<int:pk>/sales-network-update/', SalesNetworkUpdate.as_view(), name='sales-network-update'),
    path('sales-networks/', SalesNetworkList.as_view(), name='sales-networks'),
    path('<int:pk>/info-sales-network/', SalesNetworkRetrieve.as_view(), name='info-sales-network'),
    path('<int:pk>/destroy-sales-network/', SalesNetworkDestroy.as_view(), name='destroy-sales-network'),
]
