from django.db import models
from django.contrib.auth.models import User

class AttendanceRecord(models.Model):
    status_choices = [
        ('Present', 'Present'),
        ('Absent', 'Absenet'),
        ('On Leave', 'On Leave'),
    ]
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=10, choices=status_choices)
    date = models.DateField()

    class Meta:
        unique_together = ('employee', 'date')
    def __str__(self):
        return f"{self.employee.username} - {self.date}"
