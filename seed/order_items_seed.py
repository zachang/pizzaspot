import factory
from factory.django import DjangoModelFactory

from order.models import OrderItem
from seed.pizza_seed import PizzaFactory


class OrdeItemFactory(DjangoModelFactory):
    class Meta:
        model = OrderItem
    pizza = factory.SubFactory(PizzaFactory)
