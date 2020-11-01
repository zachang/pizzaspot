from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for user Customer model"""

    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=Customer.objects.all(),
            message='A user with that email already exists.',
        )],
    )

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'username': {
                'min_length': 1,
                'max_length': 50,
                'allow_blank': False,
                'required': True,
            },
            'email': {'required': True},
            'password': {
                'write_only': True,
                'min_length': 6
            },
        }

    def create(self, validated_data):
        customer = Customer(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        customer.set_password(validated_data['password'])
        customer.save()
        return customer

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.address = validated_data.get("address", instance.address)
        instance.save()
        return instance
