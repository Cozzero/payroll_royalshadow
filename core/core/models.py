from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.DecimalField(max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class meta:
        app_label = 'core'
    def __str__(self):
        return super().__str__()
    

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=32, null = False, blank = False)
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choice = [
        ('admin', 'Admin')
        ('HR', 'HR')
        ('employee', 'Employee')
    ])
   
    
