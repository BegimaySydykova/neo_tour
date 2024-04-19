from rest_framework import serializers

from .models import TourSeason, Tour, TourCategory, TourReview

class TourReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourReview
        fields = '__all__'

class TourSerializer(serializers.ModelSerializer):
    reviews = TourReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'

class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = '__all__'

class TourSeasonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TourSeason
        fields = '__all__'