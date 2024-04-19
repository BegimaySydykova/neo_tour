from django.urls import path
from .views import (
    TourListApiView,
    TourDetailApiView, 
    TourCategoryListApiView, 
    TourCategoryDetailApiView, 
    TourSeasonListApiView, 
    TourSeasonDetailApiView,
    TourReviewCreateApiView,
    )

urlpatterns = [
    path('', TourListApiView.as_view(), name='tour-list'),
    path('<int:pk>/', TourDetailApiView.as_view(), name='tour-detail'),

    path('tour_category/', TourCategoryListApiView.as_view(), name='tour-category-list'),
    path('tour_category/<int:pk>/', TourCategoryDetailApiView.as_view(), name='tour-category-detail'),

    path('tour_season/', TourSeasonListApiView.as_view(), name='tour-season-list'),
    path('tour_season/<int:pk>/', TourSeasonDetailApiView.as_view(), name='tour-season-detail'),

    path('reviews/create/', TourReviewCreateApiView.as_view(), name='tour-review-create'),
]
