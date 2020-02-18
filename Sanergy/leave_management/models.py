from django.db import models

from employee.models import Employee


class Leave_Entitlement_Type(models.Model):
    Id = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=50, blank=False)
    Leave_Type = models.CharField(max_length=50, blank=False)
    Leave_Group = models.CharField(max_length=50, blank=False)
    
class LeaveAccruals(models.Model):
    Days_Accrued = models.CharField(max_length=100, blank=False)
    Days_Worked = models.CharField(max_length=100, blank=False, null=True )
    Employee = models.CharField(max_length=100, blank=True)
    Leave_Entitlement_Utilization = models.CharField(max_length=100, blank=True)
    Period = models.CharField(max_length=100, blank=False, null=True )


class EmployeeLeaveRequest(models.Model):
    Id = models.CharField(max_length=400, blank=False, null=True)
    approval_status = models.CharField(max_length=400, blank=False, null=True)
    comments = models.CharField(max_length=400, blank=False, null=True)
    coverage_plans = models.CharField(max_length=400, blank=False, null=True)
    department_team_lead = models.CharField(max_length=400, blank=False, null=True)
    employee = models.CharField(max_length=400, blank=False, null=True)
    employee_s_department = models.CharField(max_length=400, blank=False, null=True)
    HR_approve_cancellation = models.CharField(max_length=400, blank=False, null=True)
    leave_approved = models.CharField(max_length=400, blank=False, null=True)
    leave_end_date = models.CharField(max_length=400, blank=False, null=True)
    leave_entitlement_utilization = models.CharField(max_length=400, blank=False, null=True)
    leave_start_date = models.CharField(max_length=400, blank=False, null=True)
    leave_started = models.CharField(max_length=400, blank=False, null=True)
    leave_type = models.CharField(max_length=400, blank=False, null=True)
    line_manager_account = models.CharField(max_length=400, blank=False, null=True)
    line_manager_approve_cancellation = models.CharField(max_length=400, blank=False, null=True)
    next_step = models.CharField(max_length=400, blank=False, null=True)
    next_step_due_date = models.CharField(max_length=400, blank=False, null=True)
    no_of_approved_leave_days = models.CharField(max_length=400, blank=False, null=True)
    no_of_leave_days_requested = models.CharField(max_length=400, blank=False, null=True)
    request_from_VFP = models.CharField(max_length=400, blank=False, null=True)
    sick_leave_doc_attached = models.FileField(upload_to='sick_leave_documents', null=True, blank=False)
    stage = models.CharField(max_length=400, blank=False, null=True)
    startEndDate = models.CharField(max_length=400, blank=False, null=True)


    def __str__(self):
        return self.comments

class SanergyCalendar(models.Model):
    Date = models.CharField(max_length=100, null=True, blank=True)
    Decsritption = models.CharField(max_length=300, null=True, blank=True)
    isBusinessDay = models.BooleanField(null=True, blank=True)
    isBusinessDayInclSat = models.BooleanField(null=True, blank=True)
    isHoliday = models.BooleanField(null=True, blank=True)
    isWeekend = models.BooleanField(null=True, blank=True)
    isWeekend_or_Holiday = models.BooleanField(null=True, blank=True)
    Weekday_Name = models.CharField(max_length=100, null=True, blank=True)
    Weekday_No = models.PositiveIntegerField(null=True, blank=True)
