import factory
from factory.django import DjangoModelFactory
from faker import Factory


from customer.models import Customer

faker = Factory.create()


class CustomerFactory(DjangoModelFactory):
    class Meta:
        model = Customer
    username = factory.LazyAttribute(lambda _: faker.user_name())
    email = factory.LazyAttribute(lambda _: faker.email())
    password = factory.LazyAttribute(lambda _: faker.password())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
    address = factory.LazyAttribute(lambda _: faker.address())
