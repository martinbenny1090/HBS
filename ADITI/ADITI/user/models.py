from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_hotel = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, null=True)


class Userdetails(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateTimeField()
    email = models.CharField(max_length=20, null=True, blank=True)
    PhNumber = models.CharField(max_length=20, null=True, blank=True)
    Id_Proof = models.ImageField()

    def __str__(self):
        return self.name