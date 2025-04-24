from django.contrib import admin

from electronics_sales.models import Contacts, Product, SalesNetwork


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'country', 'city', 'street', 'house_number',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'model', 'release_date',)


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_point', 'contacts', 'supplier', 'debt',)
