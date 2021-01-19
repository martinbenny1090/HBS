from django.contrib import admin
from .models import Room, Booking, Cities, Popularlocations, Hotels
# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Cities)
admin.site.register(Popularlocations)
admin.site.register(Hotels)
