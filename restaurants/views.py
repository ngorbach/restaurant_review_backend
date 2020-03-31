from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class ListRestaurantView(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(name__icontains=self.request.query_params.get('search', ''))


class CreateRestaurantView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# class ListAllByCategoryView(ListAPIView):
#     queryset = Restaurant.category.all()
#     serializer_class = RestaurantSerializer


class RetrieveUpdateDestroyRestaurantView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_url_kwarg = 'restaurant_id'
