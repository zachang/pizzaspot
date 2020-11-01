from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from pizza.models import Pizza
from seed.topping_seed import ToppingFactory
from seed.pizza_seed import PizzaFactory


class CustomerTestCase(APITestCase):
    """Test for customer api"""

    def setUp(self):
        self.client = APIClient()
        self.topping_1 = ToppingFactory(name='Pepperoni')
        self.topping_2 = ToppingFactory(name='Mushroom')
        self.pizza = PizzaFactory(flavor='marinara', size='sm', price=2.99,
                                  toppings=[self.topping_1, self.topping_2])
        self.url = reverse('pizza:pizza-list')

    def test_create_topping_successful(self):
        """Verify that a topping can be created"""

        pizza_data = {
            "flavor": "margarita",
            "size": "sm",
            "toppings": [self.topping_1.id, self.topping_2.id],
            "price": "4.99"
        }

        response = self.client.post(self.url, pizza_data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(str(self.pizza), self.pizza.flavor)
        self.assertEqual(response.data['pizzas']['flavor'], pizza_data['flavor'])

    def test_create_pizza_unsuccessful(self):
        """Verify that a pizza creation failed for wrong input format"""

        pizza_data = {
            'flavor': 'salami',
        }

        response = self.client.post(self.url, pizza_data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_retrieve_pizzas_successful(self):
        """Verify that all pizzas can be retrieved"""
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertContains(response, self.pizza.flavor)
        self.assertEqual(len(response.data), Pizza.objects.count())

    def test_single_pizza_successful(self):
        """Verify that a single pizza can be retrieved"""
        response = self.client.get(reverse('pizza:pizza-detail', args=(self.pizza.id,)), format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['flavor'], self.pizza.flavor)
