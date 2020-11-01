from django.db import models


class Pizza(models.Model):
    # allowed pizza sizes
    LARGE = 'lg'
    MEDIUM = 'md'
    SMALL = 'sm'

    # allowed pizza flavours
    MARGARITA = 'margarita'
    MARINARA = 'marinara'
    SALAMI = 'salami'

    PIZZA_SIZES = [
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
    ]

    PIZZA_FLAVORS = [
        (MARGARITA, 'Margarita'),
        (MARINARA, 'Marinara'),
        (SALAMI, 'Salami'),
    ]

    flavor = models.CharField(
        max_length=9,
        choices=PIZZA_FLAVORS,
        default=SALAMI,
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(
        max_length=2,
        choices=PIZZA_SIZES,
        default=SMALL,
    )
    toppings = models.ManyToManyField('Topping', related_name='pizzas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("flavor", "size"),)

    def __str__(self):
        return self.flavor


class Topping(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

