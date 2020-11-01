from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from pizza.models import Topping
from seed.topping_seed import ToppingFactory


class CustomerTestCase(APITestCase):
    """Test for customer api"""

    def setUp(self):
        self.client = APIClient()
        self.topping = ToppingFactory(name='Pepperoni')
        self.url = reverse('pizza:topping-list')

    def test_create_topping_successful(self):
        """Verify that a topping can be created"""

        topping_data = {
            'name': 'Mushrooms',
        }

        response = self.client.post(self.url, topping_data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(str(self.topping), self.topping.name)
        self.assertEqual(response.data['toppings']['name'], topping_data['name'])

    def test_create_topping_unsuccessful(self):
        """Verify that a topping creation failed for wrong input format"""

        topping_data = {
            'name': '',
        }

        response = self.client.post(self.url, topping_data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_retrieve_toppings_successful(self):
        """Verify that all toppings can be retrieved"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertContains(response, self.topping.name)
        self.assertEqual(len(response.data), Topping.objects.count())

    def test_single_topping_successful(self):
        """Verify that a single topping can be retrieved"""
        response = self.client.get(reverse('pizza:topping-detail', args=(self.topping.id,)), format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['name'], self.topping.name)
