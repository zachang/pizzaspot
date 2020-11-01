import factory
from factory.django import DjangoModelFactory


from pizza.models import Topping


class ToppingFactory(DjangoModelFactory):
    class Meta:
        model = Topping
    name = factory.Faker('name')
