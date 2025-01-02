from django.contrib import admin
from .models import Client,Court,Reservation,Payment

admin.site.register(Client)
admin.site.register(Court)
admin.site.register(Reservation)
admin.site.register(Payment)
# Register your models here.
