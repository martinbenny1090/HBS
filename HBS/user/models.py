from django.db import models
from django.conf import settings

# Create your models here.

class Popularlocations(models.Model):
    p_id = models.AutoField(primary_key=True)
    places = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.p_id}.{self.places}'

class Hotels(models.Model):
    h_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Popularlocations, on_delete=models.CASCADE)
    h_name = models.CharField(max_length=300, null=True, blank=True)
    landmark = models.CharField(max_length=300, blank=True)
    phone_no = models.CharField(max_length=12)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f'{self.h_id} {self.h_name}'


class Room(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100, blank=True)
    room_no = models.CharField(max_length=50, blank=True)
    price = models.FloatField() 
    discount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    image = models.FileField(blank=True)
    image1 = models.FileField(blank=True)
    image2 = models.FileField(blank=True)
    image3 = models.FileField(blank=True)
    description = models.TextField(default="")

    def __str__(self):
        return f'{self.hotel}. {self.room_type}. {self.room_no}'


class Booking(models.Model):
    b_id = models.AutoField(primary_key=True)
    persion_name = models.CharField(max_length=500)
    Phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=250)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    payment = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.persion_name

