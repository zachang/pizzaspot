from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    address = models.CharField(max_length=200, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    image = models.ImageField(upload_to="images/", blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

