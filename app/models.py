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
    location = models.CharField(max_length=100, choices=[('Barangay San Nicolas 3 Court','Barangay San Nicolas 3 Phase 1'),('Barangay Molino 3 Court','Barangay Molino 3 Phase 2')])
    date = models.DateField()
    available = models.CharField(max_length=100, choices=[('Available','Available'),('Not Available','Not Available')])
    
    def __str__(self):
        return f"{self.location}"

    def get_absolute_url(self):
        return reverse("court_detail", kwargs={"pk": self.pk})

class Reservation(models.Model):
    reservation_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey(Court, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.reservation_date}"

    def get_absolute_url(self):
        return reverse('reservation_detail', kwargs={"pk": self.pk})

class Payment(models.Model):
    amount = models.CharField(max_length=100)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=100, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])  

    def get_absolute_url(self):
        return reverse("payment_detail", kwargs={"pk": self.pk})      

class Feedback(models.Model):
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.rating}"   

    def get_absolute_url(self):
        return reverse('feedback_detail', kwargs={"pk": self.pk})      

class BookingHistory(models.Model):
    rating = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    reservation_date = models.ForeignKey(Reservation, on_delete=models.CASCADE) 
    location = models.ForeignKey(Court, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('bookingHistory_detail', kwargs={"pk": self.pk})
