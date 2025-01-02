from django.db import models
from django.urls import reverse

class Client(models.Model):
    client_Id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    sex = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.TextField(max_length=100)

class Court(models.Model):
    court_Id = models.AutoField(primary_key=True)
    courtStatus = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    available = models.BooleanField(default=False)

class Reservation(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('reservation_detail', kwargs={"pk": self.pk})

class Payment(models.Model):
    amount = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])

   
