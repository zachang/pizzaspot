from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
)

from customer.models import Customer
from seed.customer_seed import CustomerFactory


class CustomerTestCase(APITestCase):
    """Test for customer api"""

    def setUp(self):
        self.client = APIClient()
        self.customer = CustomerFactory()
        self.url = reverse("customer:customer-list")

    def test_retrieve_customers_successful(self):
        """Verify that all customers can be retrieved"""
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), Customer.objects.count())
        self.assertEqual(str(self.customer), self.customer.username)

    def test_single_customer_successful(self):
        """Verify that a single customer can be retrieved"""
        response = self.client.get(reverse("customer:customer-detail", args=(self.customer.id,)), format="json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['username'], self.customer.username)

    def test_create_customer_successful(self):
        """Verify that a single customer can be retrieved"""

        customer_data = {
            "username": "kingsy",
            "password": "phrase908",
            "email": "kingsy@gmail.com",
        }

        response = self.client.post(self.url, customer_data, format="json")
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data["users"]["username"], customer_data["username"])

