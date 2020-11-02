from rest_framework import serializers

from customer.serializers import CustomerSerializer
from order.models import Order, OrderItem
from pizza.serializers import PizzaSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for creating OrderItem instance"""

    pizza = PizzaSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'created_at', 'order', 'pizza', 'quantity', 'updated_at']
        extra_kwargs = {
            'order': {
                'read_only': True
            }
        }

    def update(self, instance, validated_data):
        if instance.order.delivery_status in ['pending', 'preparing']:
            instance.quantity = validated_data.get("quantity", instance.quantity)
            instance.save()
        return instance


class OrderListSerializer(serializers.ModelSerializer):
    """Serializer for listing Order instance"""
    customer = CustomerSerializer(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        if instance.delivery_status in ['pending', 'preparing']:
            instance.cancel_reason = validated_data.get("cancel_reason", instance.cancel_reason)
            instance.checkout_status = bool(validated_data.get("checkout_status", instance.checkout_status))
            instance.delivery_address = validated_data.get("delivery_address", instance.delivery_address)
            instance.delivery_status = validated_data.get("delivery_status", instance.delivery_status)
            instance.phone_number = validated_data.get("phone_number", instance.phone_number)
            instance.save()
        return instance


class AddOrderSerializer(serializers.ModelSerializer):
    """Serializer for creating Order instance"""
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'


class CheckoutSerializer(serializers.ModelSerializer):
    """Serializer for order checkout"""

    class Meta:
        model = Order
        fields = ['checkout_status', 'delivery_address', 'phone_number']

    def update(self, instance, validated_data):
        instance.delivery_address = validated_data.get("delivery_address", instance.delivery_address)
        instance.checkout_status = bool(validated_data.get("checkout_status", instance.checkout_status))
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.save()
        return instance

