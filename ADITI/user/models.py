from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_hotel = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, null=True)