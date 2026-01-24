from django.db import models
from django.contrib.auth.models import User
class SalaryRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_records')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.amount} on {self.date}"
