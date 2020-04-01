from django.shortcuts import render
from .models import Review
#Create your views here.

from .serializer import ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import get_user_model
User = get_user_model()

class ListCreateReviewView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        #serializer.save(buyer=self.request.user)
        serializer.save()

class GetUpdateDeleteReview(RetrieveUpdateDestroyAPIView):
        queryset = Review.objects.all()
        serializer_class = ReviewSerializer
        lookup_url_kwarg = 'review_id'

class ListReviewsUser(ListAPIView):
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(user__id=user_id)

class ListReviewsRestaurant(ListAPIView):
    serializer_class = ReviewSerializer
    lookup_url_kwarg = 'restaurant_id'

    def get_queryset(self):
        restaurant_id = self.kwargs.get("restaurant_id")
        return Review.objects.filter(restaurant__id=restaurant_id)