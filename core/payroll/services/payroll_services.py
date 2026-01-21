from calendar import monthrange
from decimal import Decimal
from payroll.models import AttendanceRecord, SalaryRecord, userProfile


# def month_days(year, month):
#     return monthrange(year, month)[1]

# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))
# days_in_month = monthrange(year, month)[1]
# gross_salary = []
# employee_id = []
# user_name = []
# present_days = []

# n = int(input("Enter number of employees: "))
# for i in range(n):
#     employee_id.append(input("Enter employee id: "))
#     user_name.append(input("Enter user name: "))
#     present_days.append(int(input("Enter present days: ")))
#     basic_salary = 1100
#     if days_in_month <= 0:
#         raise ValueError("Total days must be greater than zero.")
#     if (present_days[i]) <= 0:
#         raise ValueError("Present days cannot be negative.")
#     if (present_days[i]) > days_in_month:
#         raise ValueError("Present days cannot exceed total days.")
    
# for j in range(n):
#     if (present_days[j] <= 26):
#         gross_salary.append(present_days[j] * (basic_salary / 26));
#         print (f"employee_id: {employee_id[j]}")
#         print (f"user_name: {user_name[j]}")
#         print (f"total_salary: {gross_salary[j]}")
#     else:
#         gross_salary.append(basic_salary + (present_days[j] - 26) * 50);
#         print (f"employee_id: {employee_id[j]}")
#         print (f"user_name: {user_name[j]}")
#         print (f"total_salary: {gross_salary[j]}")




def generate_salary(user, year, month):
    """
    Generate salary for a user for a specific month and year.
    """

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
    deductions = Decimal('200.00')      # Example fixed deductions

    # Calculate net salary based on attendance
    daily_salary = basic_salary / Decimal(total_days)
    salary_for_present_days = daily_salary * Decimal(present_days)
    net_salary = salary_for_present_days + allowances - deductions

    salary_record, created = SalaryRecord.objects.get_or_create(
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

    return salary_record