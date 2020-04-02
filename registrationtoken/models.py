from django.db import models


# Create your models here.

class EmailToken(models.Model):
    emailverification = models.EmailField()
