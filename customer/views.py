from django.shortcuts import render

# Create your views here.

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from customer.models import Customer
from customer.serializers import CustomerSerializer


@api_view()
def index(request):
    return Response({'message': 'Welcome to PizzaHut'})


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the user create and list actions
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': 'Success', 'users': serializer.data},
                status=HTTP_201_CREATED,
            )

        return Response(
            {'status': 'Failure', 'messages': serializer.errors},
            status=HTTP_400_BAD_REQUEST,
        )
