from rest_framework import serializers

from electronics_sales.models import Contacts, Product, SalesNetwork


class ContactsSerializer(serializers.ModelSerializer):
    """Сериализатор для модели контакты."""

    class Meta:
        model = Contacts
        fields = "__all__"
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для модели продукта."""

    class Meta:
        model = Product
        fields = ["id", "title", "model", "release_date"]
        extra_kwargs = {"release_date": {"format": "%d-%m-%Y"}}


class SalesNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор для модели звена сети."""

    contacts = ContactsSerializer()
    products = ProductSerializer(many=True, required=False)
    supplier = serializers.PrimaryKeyRelatedField(queryset=SalesNetwork.objects.all(), required=False, allow_null=True)

    class Meta:
        model = SalesNetwork
        fields = ["id", "title", "type_point", "contacts", "products", "supplier", "debt", "created_at"]
        read_only_fields = ["created_at"]

    def validate(self, data):
        if data.get("type_point") == "завод" and data.get("supplier"):
            raise serializers.ValidationError("Завод не может иметь поставщика.")

        return data

    def create(self, validated_data):
        contacts_data = validated_data.pop("contacts")
        products_data = validated_data.pop("products", [])

        contacts = Contacts.objects.create(**contacts_data)
        sales_network = SalesNetwork.objects.create(contacts=contacts, **validated_data)

        for product_data in products_data:
            product, _ = Product.objects.get_or_create(**product_data)
            sales_network.products.add(product)

        return sales_network

    def update(self, instance, validated_data):
        if "debt" in validated_data:
            raise serializers.ValidationError({"debt": "Изменение задолженности запрещено."})

        instance.title = validated_data.get("title", instance.title)
        instance.type_point = validated_data.get("type_point", instance.type_point)

        contacts_data = validated_data.get("contacts", {})
        contacts_serializer = ContactsSerializer(instance.contacts, data=contacts_data, partial=True)
        if contacts_serializer.is_valid():
            contacts_serializer.save()

        if "products" in validated_data:
            instance.products.clear()
            for product_data in validated_data["products"]:
                product, _ = Product.objects.get_or_create(**product_data)
                instance.products.add(product)

        instance.save()
        return instance
