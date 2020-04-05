from django.contrib.auth import get_user_model
from rest_framework import serializers

from restaurants.serializers import RestaurantNameSerializer
from users.serializers import UserNameSerializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    num_reviews_of_user = serializers.SerializerMethodField()
    comment_content = serializers.SerializerMethodField()

    #user = UserNameSerializer()
    #restaurant = RestaurantNameSerializer()

    class Meta:
        model = Review
        #exclude = ['name']
        fields = '__all__'

    @staticmethod
    def get_num_reviews_of_user(self):
        return self.user.review.all().count()

    @staticmethod
    def get_comment_content(self):
        return [(comment.text_content,comment.user.first_name,comment.user.last_name) for comment in self.comments.all()]
