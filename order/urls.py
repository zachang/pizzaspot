from django.urls import path, include
from rest_framework import routers

from .views import OrderDetail, OrderItemView, OrderList

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'orders', OrderList)
router.register(r'order', OrderDetail)
router.register(r'order-items', OrderItemView, basename='order-item')

app_name = 'order'
urlpatterns = [
    path('', include(router.urls)),
]
