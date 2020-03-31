from django.shortcuts import render
from .models import Review
#Create your views here.

from .serializer import ReviewSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from django.contrib.auth import get_user_model
User = get_user_model()

class ListCreateReview(ListCreateAPIView):
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
