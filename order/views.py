from django.db.models import F
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND

from customer.models import Customer
from order.models import Order, OrderItem
from order.serializers import AddOrderSerializer, CheckoutSerializer, OrderItemSerializer, OrderListSerializer
from pizza.models import Pizza


class OrderList(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides the order list and update actions
    """
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filterset_fields = ['delivery_status', 'customer']

    def create(self, request):
        serializer = AddOrderSerializer(data=request.data)
        if serializer.is_valid():
            pizza = get_object_or_404(Pizza, pk=request.data['pizza'])

            # TODO: replace with Auth customer when Auth is implemented (request.user)
            customer = get_object_or_404(Customer, pk=request.data['customer'])
            order = Order.objects.filter(customer=customer, checkout_status=False).last()

            if not order:
                order = serializer.save()
                OrderItem.objects.create(order=order, pizza=pizza)
            else:
                order_item = OrderItem.objects.filter(order=order, pizza=pizza)
                if order_item:
                    order_item.update(quantity=F('quantity') + 1)
                else:
                    OrderItem.objects.create(order=order, pizza=pizza)
            return Response(
                {'status': 'Success', 'message': 'successfully added to cart'},
                status=HTTP_201_CREATED,
            )

        return Response(
            {'status': 'Failed', 'message': serializer.errors},
            status=HTTP_400_BAD_REQUEST,
        )


class OrderDetail(mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    A viewset that provides the order details actions
    """

    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

    @action(detail=True, methods=['GET'])
    def track_status(self, request, pk=None):
        try:
            order = self.queryset.get(pk=pk)
            serializer = self.get_serializer(order)
            return Response(
                {'status': 'Success', 'Order': {
                    'delivery_status': serializer.data['delivery_status']}
                 },
                status=HTTP_200_OK,
            )
        except ValidationError:
            return Response(
                {'status': 'Failed', 'messages': 'Please enter a valid tracking id'},
                status=HTTP_404_NOT_FOUND,
            )

    @action(detail=True, methods=['PUT'])
    def check_out(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            serializer = CheckoutSerializer(order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {'status': 'Success', 'message': 'checkout completed'},
                    status=HTTP_200_OK,
                )
        except ValidationError:
            return Response(
                {'status': 'Failed', 'messages': 'Please enter a valid tracking id'},
                status=HTTP_404_NOT_FOUND,
            )


class OrderItemView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    A viewset that provides the order_item actions
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
