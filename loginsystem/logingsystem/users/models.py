from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('normal_user', 'Normal User'),
        ('hotel_admin', 'Hotel Admin'),
        ('main_admin', 'Main Admin'),
    ]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='normal_user')

    def __str__(self):
        return self.username