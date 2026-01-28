from calendar import monthrange
from decimal import Decimal
from userprofile.models import userProfile
from attendance.models import AttendanceRecord
from salary.models import salaryRecord
from payroll.models import payroll

def generate_salary(user, year, month):
    profile = userProfile.objects.get(user=user)
    attendance_records = AttendanceRecord.objects.filter(
        user=user,
        date__year=year,
        date__month=month
    )

    total_days = monthrange(year, month)[1]
    present_days = attendance_records.count()

    basic_salary = Decimal('3000.00')  # Example fixed basic salary
    allowances = Decimal('500.00')      # Example fixed allowances
    deductions = Decimal('200.00')      # later can be dynamic

    # Calculate net salary based on attendance
    daily_salary = basic_salary / Decimal(total_days)
    salary_for_present_days = daily_salary * Decimal(present_days)
    net_salary = salary_for_present_days + allowances - deductions

    salary_record, created = salaryRecord.objects.get_or_create(
        user=user,
        name=profile.name,
        employee_id=profile.employee_id,
        defaults={
            'basic_salary': basic_salary,
            'allowances': allowances,
            'deductions': deductions,
            'net_salary': net_salary,
            'pay_date': f"{year}-{month}-25"  # Assuming pay date is 25th of the month
        }
    )

    if not created:
        # Update existing record
        salary_record.basic_salary = basic_salary
        salary_record.allowances = allowances
        salary_record.deductions = deductions
        salary_record.net_salary = net_salary
        salary_record.pay_date = f"{year}-{month}-25"
        salary_record.save()


    if created:
        # Create payroll record
        payroll.objects.create(
            user=user,
            name=profile.name,
            employee_id=profile.employee_id,
            month=f"{year}-{month}",
            total_present_days=present_days,
            net_salary=net_salary
        )

        return salary_record.present_days, salary_record.net_salary