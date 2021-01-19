from django.db import models
from django.conf import settings

# Create your models here.
class Cities(models.Model):
    c_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.city}'

class Popularlocations(models.Model):
    p_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    places = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return f'{self.places} in {self.city}'

class Hotels(models.Model):
    h_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Popularlocations, on_delete=models.CASCADE)
    h_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.h_id} {self.h_name}'


class Room(models.Model):
    room_categorites = (
        ('YAC',  'AC'),
        ('NAC',  'NON-AC'),
        ('DEL',  'DELIXE'),
        ('KIN',  'KING'),
        ('QUE',  'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=room_categorites)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    bed = models.IntegerField()
    Capacity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.number}.{self.category} with {self.bed} beds for {self.Capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has book'