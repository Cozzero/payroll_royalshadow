from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from payroll.models import payroll
from userprofile.models import userProfile
from salary.models import SalaryRecord
from attendance.models import AttendanceRecord


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        userProfile.objects.create(user=instance, name=instance.username)
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
@receiver(post_save, sender=AttendanceRecord)
def update_attendance_record(sender, instance, created, **kwargs):
    if created:
        profile = userProfile.objects.get(user=instance.user)
        instance.name = profile.name
        instance.employee_id = profile.employee_id
        instance.save()
@receiver(post_save, sender=SalaryRecord)
def update_salary_record(sender, instance, created, **kwargs):
    if created:
        profile = userProfile.objects.get(user=instance.user)
        instance.name = profile.name
        instance.employee_id = profile.employee_id
        instance.save()
@receiver(post_save, sender=payroll)
def update_payroll_record(sender, instance, created, **kwargs):
    if created:
        profile = userProfile.objects.get(user=instance.user)
        instance.name = profile.name
        instance.employee_id = profile.employee_id
        instance.save()
        