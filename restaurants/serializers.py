from rest_framework import serializers

from restaurants.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    num_ratings = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = '__all__'

    @staticmethod
    def get_ratings(self):
        return [review.rating for review in self.review.all()]

    @staticmethod
    def get_num_ratings(self):
        return len([review.rating for review in self.review.all()])

    @staticmethod
    def get_avg_rating(self):
        ratings = [review.rating for review in self.review.all()]
        return sum(ratings)/len(ratings) if len(ratings) != 0 else 0

    @staticmethod
    def get_category_name(self):
        return self.category.name

class RestaurantNameSerializer(serializers.ModelSerializer):

        class Meta:
            model = Restaurant
            fields = ['name']