from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.


# CREATE NEW REVIEW
class Review(models.Model):
    id = models.IntegerField(default=1, primary_key=True)
    text_content = models.TextField(default="enter text")
    rating = models.IntegerField(default=1)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='review', on_delete=models.CASCADE)
    #restaurant = models.ForeignKey(to=settings.Restaurant, related_name='review', on_delete=models.CASCADE)

