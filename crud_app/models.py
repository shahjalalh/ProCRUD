from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    NEWSLETTER_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    house_no = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    newsletter = models.CharField(max_length=1, choices=NEWSLETTER_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(blank=True, null=True)

    def modified(self):
        self.modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email
