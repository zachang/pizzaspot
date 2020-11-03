import factory
from factory.django import DjangoModelFactory


from pizza.models import Pizza


class PizzaFactory(DjangoModelFactory):
    class Meta:
        model = Pizza
    flavor = factory.Faker('flavor')
    price = factory.Faker('price')
    size = factory.Faker('size')

    @factory.post_generation
    def toppings(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of toppings were passed in, use them
            for topping in extracted:
                self.toppings.add(topping)
