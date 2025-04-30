from django.contrib import admin
from django.utils.html import format_html

from electronics_sales.models import Contacts, Product, SalesNetwork


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )
    list_filter = ("country", "city")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "model",
        "release_date",
    )
    search_fields = ("title", "model")


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "type_point", "display_supplier", "contacts", "debt", "created_at")
    list_filter = ("contacts__city",)
    actions = ["clear_debt"]

    def display_supplier(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="{}">{}</a>',
                f"/admin/electronics_sales/salesnetwork/{obj.supplier.id}/change/",
                obj.supplier.title,
            )
        return "-"

    display_supplier.short_description = "Поставщик"

    @admin.action(description="Очистить задолженность у выбранных объектов")
    def clear_debt(self, request, queryset):
        updated = queryset.update(debt=0)
        self.message_user(request, f"Задолженность очищена у {updated} объектов")
