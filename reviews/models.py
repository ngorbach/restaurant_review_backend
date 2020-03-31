from django.db import models
from datetime import datetime
from django.conf import settings
from restaurants.models import Restaurant
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

# CREATE NEW REVIEW
class Review(models.Model):
    text_content = models.TextField()
    rating = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='review', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, related_name='review', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)