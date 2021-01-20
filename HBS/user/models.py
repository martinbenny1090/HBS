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
    landmark = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.h_id} {self.h_name}'

class Room_categories(models.Model):
    ca_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=150)
    

    def __str__(self):
        return f'{self.hotel.h_name}. {self.categorie}'



class Room(models.Model):
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    category = models.ForeignKey(Room_categories, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    no_bed = models.IntegerField()
    no_guest =models.IntegerField()
    t_number = models.IntegerField()
    price = models.IntegerField()
    image = models.FileField(blank=True)

    def __str__(self):
        return f'{self.hotel}.{self.category} with {self.no_bed} beds for {self.no_guest} people'

class Images(models.Model):
    room = models.ForeignKey(Room, default=None, on_delete=models.CASCADE)
    image_1 = models.FileField()
    image_2 = models.FileField()
    image_3 = models.FileField()
    image_5 = models.FileField()

    def __str__(self):
        return self.room.title


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} has book'