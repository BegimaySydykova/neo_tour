from django.db import models

# Create your models here.

class TourCategory(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Tour(models.Model):
    tour_photo = models.ImageField(upload_to="tours_photos/")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField()
    popularity = models.IntegerField(default=0) 
    is_favorite = models.BooleanField(default=False)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class TourSeason(models.Model):
    SPRING = "SPRING"
    AUTUMN = "AUTUMN"
    SUMMER = "SUMMER"
    WINTER = "WINTER"
    SEASON_CHOICES = (
        (SPRING, "Spring"),
        (AUTUMN, "Autumn"),
        (SUMMER, "Summer"),
        (WINTER, "Winter"),
    )
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    season = models.CharField(
        max_length=6,
        choices=SEASON_CHOICES,
        default=SUMMER,
    )

    def __str__(self):
        return f"{self.tour.name} - {self.season}"
    
class TourReview(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_photo = models.ImageField(upload_to='user_photos/', null=True)
    comment = models.TextField()

    def __str__(self):
        return f"Review for tour {self.tour.name} by {self.user_name}"