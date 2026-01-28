from django.db import models
from django.contrib.auth.models import User
class salaryRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salary_records')
    employee_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()


    class Meta:
        unique_together = ['employee_id', 'amount', 'date']
    def __str__(self):
        return f"{self.user.username} - {self.employee_id} - {self.amount} on {self.date}"
