from django.test import TestCase

# Create your tests here.
class Restaurant(models.Model):
    name = models.CharField(max_length=250)
