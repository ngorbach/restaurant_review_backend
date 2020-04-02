from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserNameSerializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    user = UserNameSerializer()

    class Meta:
        model = Review
        #exclude = ['name']
        fields = '__all__'
