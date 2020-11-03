import uuid
from django.db import models

from customer.models import Customer
from pizza.models import Pizza


class Order(models.Model):
    # allowed tracking statuses
    CANCELLED = 'cancelled'
    OUT_FOR_DELIVERING = 'delivering'
    DELIVERED = 'delivered'
    NO_CHECKOUT = 'pending'
    PREPARING = 'preparing'
    READY = 'ready'

    TRACKING_STATUS = [
        (CANCELLED, 'cancelled'),
        (OUT_FOR_DELIVERING, 'delivering'),
        (DELIVERED, 'delivered'),
        (NO_CHECKOUT, 'pending'),
        (PREPARING, 'preparing'),
        (READY, 'ready'),
    ]

    cancel_reason = models.TextField(null=True)
    checkout_status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    delivery_address = models.TextField(null=True)
    delivery_status = models.CharField(
        max_length=10,
        choices=TRACKING_STATUS,
        default=NO_CHECKOUT,
    )
    phone_number = models.CharField(max_length=14, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_total_cost(self):
        return sum(float(item.get_cost) for item in self.order_items.all())

    def __str__(self):
        return self.delivery_status


class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_order_items")
    quantity = models.PositiveIntegerField(default=1)

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_cost(self):
        return self.pizza.price * self.quantity

    def __str__(self):
        return str(self.quantity)
