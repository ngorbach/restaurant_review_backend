from django.db import models

# Create your models here.

DAYS = [
    (1, _('Sunday')),
    (2, _('Monday')),
    (3, _('Tuesday')),
    (4, _('Wednesday')),
    (5, _('Thursday')),
    (6, _('Friday')),
    (7, _('Saturday')),
]

PRICE = [
    ('LOW', '$'),
    ('MEDIUM', '$$'),
    ('HIGH', '$$$'),
]

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=500)
    country = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.IntegerField(max_length=10)
    website = models.URLField(max_length=250)
    phone = models.IntegerField(max_length=10)
    # https://pypi.org/project/django-phone-field/
    email = models.EmailField(max_length=100)
    opening_days = models.IntegerField(choices=DAYS)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    price_level = models.CharField(choices=PRICE)
    # image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post {self.id} by {self.user}'
