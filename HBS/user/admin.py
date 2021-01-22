from django.contrib import admin
from .models import Room, Booking, Popularlocations, Hotels, Room_categories, Images
# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Popularlocations)
admin.site.register(Hotels)
admin.site.register(Room_categories)
admin.site.register(Images)