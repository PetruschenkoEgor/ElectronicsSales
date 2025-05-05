from django.db import models
from rest_framework.exceptions import ValidationError


class Contacts(models.Model):
    """Модель контактов поставщика."""

    email = models.EmailField(verbose_name="Почта")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=250, verbose_name="Улица")
    house_number = models.CharField(max_length=100, verbose_name="Номер дома")

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"{self.email}, {self.country}, {self.city}, {self.street}, {self.house_number}"


class Product(models.Model):
    """Модель продукта."""

    title = models.CharField(max_length=250, verbose_name="Название продукта")
    model = models.CharField(max_length=250, verbose_name="Модель продукта")
    release_date = models.DateField(verbose_name="Дата выхода продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукция"

    def __str__(self):
        return f"{self.title} - {self.model}"


class SalesNetwork(models.Model):
    """Модель звена сети (завод, розничная сеть, ИП)."""

    CHOICE_TYPE = (
        ("завод", "Завод"),
        ("розничная сеть", "Розничная сеть"),
        ("индивидуальный предприниматель", "Индивидуальный предприниматель"),
    )

    title = models.CharField(max_length=250, verbose_name="Название звена")
    type_point = models.CharField(max_length=40, verbose_name="Тип звена", choices=CHOICE_TYPE)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, verbose_name="Контакты поставщика")
    products = models.ManyToManyField(Product, verbose_name="Продукты поставщика", blank=True)
    supplier = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Поставщик продукции",
        blank=True,
        null=True,
        related_name="suppliers",
    )
    debt = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="Задолженность перед поставщиком", default=0.00
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"

    def clean(self):
        """Валидация данных."""

        if self.type_point == "завод" and self.supplier:
            raise ValidationError("Завод не может иметь поставщика.")

        if self.supplier and self.supplier == self:
            raise ValidationError("Объект не может ссылаться на себя.")

    def __str__(self):
        return f"{self.title}, {self.type_point}, {self.debt}"
