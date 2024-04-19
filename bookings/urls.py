from django.urls import path

from .views import TourBookingListApiView, TourBookingDetailApiView, TourBookingCreateApiView


urlpatterns = [
    path('', TourBookingListApiView.as_view(), name='tour-booking-list'),
    path('<int:pk>/', TourBookingDetailApiView.as_view(), name='tour-booking-detail'),

    path('create/', TourBookingCreateApiView.as_view(), name='tour-booking-create'),
]
