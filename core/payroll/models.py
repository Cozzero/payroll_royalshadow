from django.db import models
from django.contrib.auth.models import User

class PayrollRecord(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
        return f"{self.user.username} - {self.department}"

class Attendance(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)  # True for present, False for absent'

def __str__(self):
        return f"{self.user.username} - {self.date} - {'Present' if self.status else 'Absent'}"

class SalaryPayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    method = models.CharField(max_length=50)  # e.g., 'Bank Transfer', 'Cash'
def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.payment_date}"

