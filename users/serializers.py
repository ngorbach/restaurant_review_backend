from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    num_reviews = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']

    @staticmethod
    def get_num_reviews(self):
        return self.review.count()


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']