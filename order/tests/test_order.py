from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND)

from order.models import Order
from seed.customer_seed import CustomerFactory
from seed.order_seed import OrderFactory
from seed.order_items_seed import OrdeItemFactory
from seed.pizza_seed import PizzaFactory
from seed.topping_seed import ToppingFactory


class OrderTestCase(APITestCase):
    """Test for customer api"""

    def setUp(self):
        pass
        self.client = APIClient()
        self.topping = ToppingFactory()
        self.customer = CustomerFactory()
        self.pizza = PizzaFactory(flavor='salima', size='sm', price=2.99,
                                  toppings=[self.topping])
        self.order = OrderFactory(customer=self.customer)
        self.order_item = OrdeItemFactory(order=self.order, pizza=self.pizza)

        # test urls
        self.order_url = reverse('order:order-list')
        self.order_detail_url = reverse('order:order-detail', args=(self.order.id,))
        self.order_status_url = reverse('order:order-track-status', args=(self.order.id,))
        self.order_checkout_url = reverse('order:order-checkout', args=(self.order.id,))
        self.order_items_url = reverse('order:order-item-list')

    def test_create_order_successful(self):
        """Verify that an order can be created"""
        order_data = {
            "pizza": self.pizza.id,
            "customer": self.customer.id
        }

        response = self.client.post(self.order_url, order_data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(str(self.order), self.order.delivery_status)

    def test_create_order_unsuccessful(self):
        """Verify that an order creation failed"""
        pizza_data = {}
        response = self.client.post(self.order_url, pizza_data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_retrieve_orders_successful(self):
        """Verify that all orders can be retrieved"""
        response = self.client.get(self.order_url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), Order.objects.count())
        self.assertEqual(self.order.get_total_cost, 2.99)
        self.assertEqual(str(self.order_item), str(self.order_item.quantity))

    def test_single_order_successful(self):
        """Verify that a single order can be retrieved"""
        response = self.client.get(self.order_detail_url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['checkout_status'], self.order.checkout_status)

    def test_retrieve_order_items_successful(self):
        """Verify that a all order items can be retrieved"""
        response = self.client.get(self.order_items_url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(self.order_item.get_cost, 2.99)

    def test_track_status_successful(self):
        """Track delivery status for an order"""
        response = self.client.get(self.order_status_url, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['order']['delivery_status'], self.order.delivery_status)

    def test_track_status_usnsuccessful(self):
        """Track delivery failure for invalid order_id"""
        response = self.client.get(reverse('order:order-track-status', args=('909uutt',)), format='json')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_checkout_successful(self):
        """Checkout an order"""
        checkout_data = {
            "delivery_address": "Lawrence Estate",
            "checkout_status": "True",
            "phone_number": "090999999977",
        }
        response = self.client.put(self.order_checkout_url, checkout_data, format='json')
        order = Order.objects.get(id=self.order.id)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertTrue(order.checkout_status)

    def test_checkout_unsuccessful(self):
        """Checkout failure for invalid order_id"""
        checkout_data = {}
        response = self.client.put(reverse('order:order-checkout', args=('954e56',)), checkout_data, format='json')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_order_successful(self):
        """Verify that a single order can be deleted"""
        response = self.client.delete(self.order_detail_url, format='json')
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

