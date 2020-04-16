from django.contrib import admin
from salesforce.testrunner.example.universal_admin import \
    register_omitted_classes

from .models import (EmployeeLeaveRequest, Leave_Entitlement_Type,
                     LeaveAccruals, SanergyCalendar)

# Register your models here.
admin.site.register(EmployeeLeaveRequest)
admin.site.register(Leave_Entitlement_Type)
admin.site.register(LeaveAccruals)
admin.site.register(SanergyCalendar)