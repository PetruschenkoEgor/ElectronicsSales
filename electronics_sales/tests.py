from django.urls import reverse
from rest_framework.test import APITestCase

from electronics_sales.models import Contacts, Product, SalesNetwork
from users.models import User


class SalesNetworkCreateTest(APITestCase):
    """Тест создания звена сети продажи электроники."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="testuser@mail.ru", password="testpass", is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.form_data = {
            "title": "Завод",
            "type_point": "завод",
            "contacts": {
                "email": "test1@mail.ru",
                "country": "Россия",
                "city": "Омск",
                "street": "Ленина",
                "house_number": "1",
            },
            "products": [{"title": "Микроволновка", "model": "свч-1", "release_date": "2024-05-05"}],
            "debt": 100000.00,
        }

    def test_sales_network_create(self):
        """Тест создания звена сети продажи электроники."""

        url = reverse("electronics_sales:sales-network-create")
        response = self.client.post(url, data=self.form_data, format="json")

        self.assertEqual(response.status_code, 201)

        self.assertEqual(SalesNetwork.objects.count(), 1)
        self.assertEqual(Contacts.objects.count(), 1)
        self.assertEqual(Product.objects.count(), 1)

        sales_network = SalesNetwork.objects.first()
        self.assertEqual(sales_network.title, "Завод")
        self.assertEqual(sales_network.type_point, "завод")
        self.assertEqual(sales_network.debt, 100000.00)

        self.assertEqual(sales_network.contacts.email, "test1@mail.ru")
        self.assertEqual(sales_network.products.first().title, "Микроволновка")


class SalesNetworkUpdateTest(APITestCase):
    """Тест редактирования звена сети продажи электроники."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="testuser@mail.ru", password="testpass", is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.contacts = Contacts.objects.create(
            email="test2@mail.ru", country="Россия", city="Омск", street="Ленина", house_number="1"
        )

        self.product = Product.objects.create(title="Микроволновка", model="свч-1", release_date="2024-05-05")

        self.sales_network = SalesNetwork.objects.create(
            title="Завод", type_point="завод", contacts=self.contacts, debt=100000.00
        )
        self.sales_network.products.add(self.product)

        self.updated_data = {
            "title": "Завод тест",
        }

    def test_sales_network_update(self):
        """Тест редактирования звена сети продажи электроники."""

        url = reverse("electronics_sales:sales-network-update", kwargs={"pk": self.sales_network.pk})
        response = self.client.patch(url, data=self.updated_data, format="json")

        self.assertEqual(response.status_code, 200)

        sales_network = SalesNetwork.objects.first()
        self.assertEqual(sales_network.title, "Завод тест")


class SalesNetworkListTest(APITestCase):
    """Тест списка звеньев сети продажи электроники."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="testuser@mail.ru", password="testpass", is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.contacts1 = Contacts.objects.create(
            email="test1@mail.ru", country="Россия", city="Омск", street="Ленина", house_number="1"
        )

        self.product = Product.objects.create(title="Микроволновка", model="свч-1", release_date="2024-05-05")

        self.sales_network1 = SalesNetwork.objects.create(
            title="Завод", type_point="завод", contacts=self.contacts1, debt=100000.00
        )
        self.sales_network1.products.add(self.product)

        self.contacts2 = Contacts.objects.create(
            email="test2@mail.ru", country="Россия2", city="Омск2", street="Ленина2", house_number="2"
        )

        self.sales_network2 = SalesNetwork.objects.create(
            title="Завод2", type_point="завод", contacts=self.contacts2, debt=100000.00
        )
        self.sales_network2.products.add(self.product)

    def test_sales_network_list(self):
        """Тест списка звеньев сети продажи электроники."""

        url = reverse("electronics_sales:sales-networks")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        sales_networks = SalesNetwork.objects.all()
        self.assertEqual(sales_networks.count(), 2)


class SalesNetworkRetrieveTest(APITestCase):
    """Тест информации о звене сети продажи электроники."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="testuser@mail.ru", password="testpass", is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.contacts = Contacts.objects.create(
            email="test1@mail.ru", country="Россия", city="Омск", street="Ленина", house_number="1"
        )

        self.product = Product.objects.create(title="Микроволновка", model="свч-1", release_date="2024-05-05")

        self.sales_network = SalesNetwork.objects.create(
            title="Завод", type_point="завод", contacts=self.contacts, debt=100000.00
        )
        self.sales_network.products.add(self.product)

    def test_sales_network_retrieve(self):
        """Тест информации о звене сети продажи электроники."""

        url = reverse("electronics_sales:info-sales-network", kwargs={"pk": self.sales_network.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        sales_network = SalesNetwork.objects.first()
        self.assertEqual(sales_network.title, "Завод")
        self.assertEqual(sales_network.type_point, "завод")
        self.assertEqual(sales_network.debt, 100000.00)

        self.assertEqual(sales_network.contacts.email, "test1@mail.ru")
        self.assertEqual(sales_network.products.first().title, "Микроволновка")


class SalesNetworkDestroyTest(APITestCase):
    """Тест удаления звена сети продажи электроники."""

    def setUp(self):
        self.user = User.objects.create_user(
            username="test", email="testuser@mail.ru", password="testpass", is_active=True
        )
        self.client.force_authenticate(user=self.user)

        self.contacts = Contacts.objects.create(
            email="test1@mail.ru", country="Россия", city="Омск", street="Ленина", house_number="1"
        )

        self.product = Product.objects.create(title="Микроволновка", model="свч-1", release_date="2024-05-05")

        self.sales_network = SalesNetwork.objects.create(
            title="Завод", type_point="завод", contacts=self.contacts, debt=100000.00
        )
        self.sales_network.products.add(self.product)

    def test_sales_network_destroy(self):
        """Тест удаления звена сети продажи электроники."""

        url = reverse("electronics_sales:destroy-sales-network", kwargs={"pk": self.sales_network.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

        sales_network = SalesNetwork.objects.all()
        self.assertEqual(sales_network.count(), 0)
