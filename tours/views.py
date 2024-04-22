from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import Tour, TourCategory, TourSeason, TourReview
from .serializers import TourSerializer, TourCategorySerializer, TourSeasonSerializer, TourReviewSerializer
# Create your views here.

class TourListApiView(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    @swagger_auto_schema(
        operation_description="Этот эндпоинт позволяет получить "
        "список постов. Вы можете применять "
        "фильтрацию по категории, а также осуществлять "
        "поиск по заголовку и содержанию постов.",
        responses={200: TourSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "category_name",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Отфильтровать посты по названию категории.",
            ),
            ]
        )
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Применение фильтров по категориям
        category_name = request.query_params.get("category_name")

        if category_name:
            queryset = queryset.filter(category__name=category_name)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TourDetailApiView(RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        reviews_serializer = TourReviewSerializer(instance.tourreview_set.all(), many=True)  # Получаем все отзывы для этого тура
        data = serializer.data
        data['reviews'] = reviews_serializer.data  # Добавляем отзывы в данные тура
        return Response(data)
    
class TourReviewCreateApiView(CreateAPIView):
    serializer_class = TourReviewSerializer
    
    def create(self, request):
        serializer = TourReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourCategoryListApiView(ListAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer

class TourCategoryDetailApiView(RetrieveAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer


class TourSeasonListApiView(ListAPIView):
    queryset = TourSeason.objects.all()
    serializer_class = TourSeasonSerializer

class TourSeasonDetailApiView(RetrieveAPIView):
    queryset = TourSeason.objects.all()
    serializer_class = TourSeasonSerializer   