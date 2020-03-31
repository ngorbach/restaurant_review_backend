from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        #exclude = ['name']
        fields = 'all'
