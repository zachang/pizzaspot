from django.urls import path, include
from rest_framework import routers

from .views import PizzaViewSet, ToppingViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'pizzas', PizzaViewSet)
router.register(r'toppings', ToppingViewSet)

app_name = 'pizza'
urlpatterns = [
    path('', include(router.urls)),
]
