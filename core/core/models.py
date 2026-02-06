from django.db import models
from django.contrib.auth.models import AbstractUser


class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class user(AbstractUser):
    ROLE_CHOICES = [
            ('admin', 'Admin')
            ('HR', 'HR')
            ('account', 'Account')
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null = True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default= 'account')

