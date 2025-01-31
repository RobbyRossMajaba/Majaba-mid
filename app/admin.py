from django.contrib import admin
from .models import Client,Court,Reservation,Payment,Feedback,BookingHistory

admin.site.register(Client)
admin.site.register(Court)
admin.site.register(Reservation)
admin.site.register(Payment)
admin.site.register(Feedback)
admin.site.register(BookingHistory)
# Register your models here.
