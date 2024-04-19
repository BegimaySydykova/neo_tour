from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import TourBooking
from .serializers import TourBookingSerializer
# Create your views here.

class TourBookingListApiView(ListAPIView):
    queryset = TourBooking.objects.all()
    serializer_class = TourBookingSerializer

class TourBookingDetailApiView(RetrieveAPIView):
    queryset = TourBooking.objects.all()
    serializer_class = TourBookingSerializer

class TourBookingCreateApiView(CreateAPIView):
    queryset = TourBooking.objects.all()

    def create(self, request):
        serializer = TourBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)