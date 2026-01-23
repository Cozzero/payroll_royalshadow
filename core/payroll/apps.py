from django.apps import AppConfig

def ready(self):
        import payroll.signals
class PayrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payroll'
