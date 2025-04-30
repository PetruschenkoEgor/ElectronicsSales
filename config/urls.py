from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("electronics_sales/", include("electronics_sales.urls", namespace="electronics_sales")),
    path("users/", include("users.urls", namespace="users")),
]
