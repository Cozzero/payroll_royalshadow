
from django.db import models
from django.contrib.auth.models import AbstractUser
from .models import Company


class user(AbstractUser):
    ROLE_CHOICES = [
            ('admin', 'Admin')
            ('HR', 'HR')
            ('account', 'Account')
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default= 'account')

