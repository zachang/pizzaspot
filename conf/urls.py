from django.contrib import admin
from django.urls import path, include

from customer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/', include('customer.urls', namespace='customer')),
    path('api/v1/', include('pizza.urls', namespace='pizza')),
    path('admin/', admin.site.urls),
]
