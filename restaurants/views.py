from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class ListCreatePostView(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_queryset(self):
        return Restaurant.objects.filter(name__icontains=self.request.query_params.get('search', ''))
