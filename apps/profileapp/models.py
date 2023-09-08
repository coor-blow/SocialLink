from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True, help_text=' username')
    email = models.EmailField(max_length=100, null=True, help_text=' email')
    password = models.CharField(max_length=128, null=True, help_text=' password')
    
    