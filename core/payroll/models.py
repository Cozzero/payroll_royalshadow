from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Employee Name')
    employee_id = models.CharField(max_length=20, unique=True, blank=False, null=False, default='enter employee id')
    phone_number = models.CharField(max_length=15)
    passport_number = models.CharField(max_length=20, blank=False, null=False, default='enter passport no')
    visa_type = models.CharField(max_length=100, blank=False, null=False, default='Packer', choices=[
        ('Packer', 'Packer'),
        ('Security', 'Security'),
        ('Telecommunication Assistant', 'Telecommunication Assistant'),
    ])

    def __str__(self):
            return f"{self.user.username} Profile"
    
class SalaryRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Employee Name')
    employee_id = models.CharField(max_length=20, unique=True, blank=False, null=False, default='enter employee id')
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)
    pay_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Salary Record for {self.user.username} on {self.pay_date}"
    
class AttendanceRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Employee Name')
    employee_id = models.CharField(max_length=20, unique=True, blank=False, null=False, default='enter employee id')
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()

    def __str__(self):
        return f"Attendance for {self.user.username} on {self.date}"
    
class payroll(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
        name = models.CharField(max_length=100, default='Employee Name')
        employee_id = models.CharField(max_length=20, unique=True, blank=False, null=False, default='enter employee id')
        month = models.CharField(max_length=20)
        total_present_days = models.IntegerField()
        net_salary = models.DecimalField(max_digits=10, decimal_places=2)
        generated_on = models.DateTimeField(auto_now_add=True)
        def __str__(self):
            return f"Payroll for {self.employee.user.username} - {self.month}"
        
