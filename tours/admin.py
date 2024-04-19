from django.contrib import admin
from .models import Tour, TourCategory, TourSeason, TourReview

# Register your models here.

admin.site.register(Tour)
admin.site.register(TourCategory)
admin.site.register(TourSeason)
admin.site.register(TourReview)