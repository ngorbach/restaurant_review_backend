from django.db import models

# Create your models here.

DAYS = [
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),
    (6, 'Friday'),
    (7, 'Saturday')
]

PRICE = [
    ('LOW', '$'),
    ('MEDIUM', '$$'),
    ('HIGH', '$$$')
]

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    website = models.URLField(max_length=250)
    phone = models.IntegerField()
    # https://pypi.org/project/django-phone-field/
    email = models.EmailField(max_length=100)
    opening_days = models.IntegerField(choices=DAYS)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    price_level = models.CharField(max_length=6, choices=PRICE)
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}: {self.name}'
