from django.db import models
from django.contrib.auth import get_user_model
from reviews.models import Review

# Create your models here.
from django.db import models

User = get_user_model()

class Comment(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    #review = models.ManyToManyField(User, related_name='review', blank=True)
    review = models.ForeignKey(to=Review, related_name='comments', on_delete=models.CASCADE)

    text_content = models.CharField(
        verbose_name='text_content',
        max_length=500,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    
    def __str__(self):
        return  f'Item {self.text_content} by {self.user}'