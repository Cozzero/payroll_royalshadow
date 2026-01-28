from django.db import models
from django.contrib.auth.models import User


class userProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, blank=False, null=False, default='enter employee id')
    department = models.CharField(choices=[
        ('Warehouse Helpers', 'Warehouse Helpers'),
        ('Security Guard', 'Security Guard'),
    ])
    visa_category = models.CharField(choices=[
        ('Packers', 'Packers'),
        ('Security', 'Security'),
        ('Team', 'Team'),
    ])
    passport_no = models.CharField(max_length=100)


    class Meta:
        unique_together = ['user', 'name', 'employee_id', 'visa_category', 'passport_no']
    def __str__(self):
        return f"{self.user.username} - {self.employee_id} - {self.visa_category} - {self.passport_no}"