from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from pizza.models import Pizza, Topping
from pizza.serializers import ListPizzaSerializer, PizzaSerializer, ToppingSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    """
    A viewset for pizza api access
    """
    def get_serializer_class(self):
        """
        Instantiates and returns the serializer_class that this view requires.
        """
        if self.action in ['list', 'retrieve']:
            serializer_class = ListPizzaSerializer
        else:
            serializer_class = PizzaSerializer
        return serializer_class

    queryset = Pizza.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": 'Success', 'pizzas': serializer.data},
                status=HTTP_201_CREATED
            )

        return Response(
            {"status": "Failure", "messages": serializer.errors},
            status=HTTP_400_BAD_REQUEST,
        )


class ToppingViewSet(viewsets.ModelViewSet):
    """
    A viewset for pizza toppings access
    """
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'status': 'Success', 'toppings': serializer.data},
                status=HTTP_201_CREATED
            )

        return Response(
            {'status': 'Failure', 'messages': serializer.errors},
            status=HTTP_400_BAD_REQUEST,
        )
