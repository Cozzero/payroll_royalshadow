from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class userProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True)
    department = models.CharField(choices=[
        ('Warehouse Helpers = Warehouse Helpers'),
        ('Security Guard = Security Guard'),
    ])
    visa_category = models.CharField(choices=[
        ('Packers = Packers')
        ('Security = Security'),
        ('Team = Team'),
    ])
    passport_no = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_full_profile(self):
        return {
            "name": self.name,
            "employee_id": self.employee_id,
            "department": self.department,
            "visa_category": self.visa_category,
            "passport_no": self.passport_no,
            
        }