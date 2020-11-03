import factory
from factory.django import DjangoModelFactory

from order.models import Order
from seed.customer_seed import CustomerFactory


class OrderFactory(DjangoModelFactory):
    class Meta:
        model = Order
    customer = factory.SubFactory(CustomerFactory)
