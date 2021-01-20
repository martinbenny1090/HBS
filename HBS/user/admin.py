from django.contrib import admin
from .models import Room, Booking, Cities, Popularlocations, Hotels, Room_categories
# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Cities)
admin.site.register(Popularlocations)
admin.site.register(Hotels)
admin.site.register(Room_categories)
