from django.urls import path, include
from rest_framework import routers

from .views import CustomerViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerViewSet)

app_name = 'customer'
urlpatterns = [
    path('', include(router.urls)),
]
