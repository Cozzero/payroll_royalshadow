from django.db import models
from django.contrib.auth.models import User

class payroll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, default='Employee Name')
    employee_id = models.CharField(max_length=20, blank=False, null=False, default='enter employee id')
    month = models.CharField(max_length=20)
    total_present_days = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    generated_on = models.DateTimeField(auto_now_add=True)


# class Meta:
#         unique_together = ['name','employee_id', 'amount', 'month']
# def __str__(self):
#        return f"{self.name} - {self.employee_id} - {self.amount} - {self.month}"
#        #return f"{self.user.username} -  {self.name} - {self.employee_id} - {self.amount} on {self.month}"


    class Meta:
        unique_together = ['employee_id', 'amount', 'month', 'generated_on']
    def __str__(self):
        return f"{self.user.username} - {self.employee_id} - {self.amount} on {self.month} - {self.generated_on}"
