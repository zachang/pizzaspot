from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from pizza.models import Pizza, Topping


class ToppingSerializer(serializers.ModelSerializer):
    """Serializer for Topping instance"""
    name = serializers.CharField(
        validators=[UniqueValidator(
            queryset=Topping.objects.all(),
            message='A topping with that name already exists.')],
    )

    class Meta:
        model = Topping
        fields = '__all__'

    def create(self, validated_data):
        return Topping.objects.create(**validated_data)


class PizzaSerializer(serializers.ModelSerializer):
    """Serializer for creating Pizza instance"""

    class Meta:
        model = Pizza
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'toppings': {'required': True}
        }


class ListPizzaSerializer(serializers.ModelSerializer):
    """Serializer for retrieving all Pizza instance"""
    toppings = ToppingSerializer(many=True, read_only=True)

    class Meta:
        model = Pizza
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

