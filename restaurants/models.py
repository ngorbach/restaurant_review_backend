from django.db import models

# Create your models here.
from multiselectfield import MultiSelectField

from categories.models import Category

DAYS = [
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday')
]

PRICE = [
    ('LOW', '$'),
    ('MEDIUM', '$$'),
    ('HIGH', '$$$')
]

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(to=Category, related_name='restaurant', on_delete=models.CASCADE)
    country = models.CharField(max_length=100,default=None,blank=True,null=True)
    street = models.CharField(max_length=100,default=None,blank=True,null=True)
    city = models.CharField(max_length=100,default=None,blank=True,null=True)
    zip = models.IntegerField(default=None,blank=True,null=True)
    website = models.URLField(max_length=250,default=None,blank=True,null=True)
    phone = models.IntegerField(default=None,blank=True,null=True)
    # https://pypi.org/project/django-phone-field/
    email = models.EmailField(max_length=100,default=None,blank=True,null=True)
    opening_days = MultiSelectField(choices=DAYS,default=None,blank=True,null=True)
    opening_time = models.TimeField(default=None,blank=True,null=True)
    closing_time = models.TimeField(default=None,blank=True,null=True)
    price_level = models.CharField(max_length=6, choices=PRICE,default=('MEDIUM', '$$'))
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.name}'

