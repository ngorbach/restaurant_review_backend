from django.shortcuts import render
from django.db.models import Avg

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

from categories.models import Category
from categories.serializer import CategorySerializer
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class ListRestaurantView(ListAPIView):
    permission_classes = []
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(name__icontains=self.request.query_params.get('search', ''))


class ListFourRestaurantsView(ListAPIView):
    permission_classes = []
    queryset = Restaurant.objects.annotate(restaurant_rating_avg=Avg("review__rating")).order_by("-restaurant_rating_avg")[:4]
    serializer_class = RestaurantSerializer


class CreateRestaurantView(CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class ListByCategoryView(ListAPIView):
    permission_classes = []
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(name__icontains=self.request.query_params.get('search', ''))


class RetrieveUpdateDestroyRestaurantView(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_url_kwarg = 'restaurant_id'


#class ListBestRestaurantsView(ListAPIView):
#    permission_classes = []
#    queryset = Restaurant.objects.all()
#    serializer_class = RestaurantSerializer

#    def get_queryset(self):
#        return Restaurant.objects.all().order_by('-review__rating')[:4]