from django.db import models
from user.models import CustomUser
# Create your models here.

class Hotel(models.Model):
    Hname = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    landmark = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.Hname


class Room(models.Model):
    HotelName  = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Rno = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    image = models.ImageField()
    img1 = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    _id = models.AutoField(primary_key=True, editable=False)
    tax = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.Rno)
