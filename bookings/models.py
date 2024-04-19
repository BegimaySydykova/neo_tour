from django.db import models

from tours.models import Tour

# Create your models here.

class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    num_people = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    additional_comments = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for tour {self.tour.name}"