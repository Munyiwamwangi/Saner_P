from django.db import models

from employee.models import Employee
class LeaveAccruals(models.Model):
    Days_Accrued = models.CharField(max_length=100, blank=False)
    Days_Worked = models.CharField(max_length=100, blank=False, null=True )
    Employee = models.CharField(max_length=100, blank=True)
    Leave_Entitlement_Utilization = models.CharField(max_length=100, blank=True)
    Period = models.CharField(max_length=100, blank=False, null=True )


class EmployeeLeaveRequest(models.Model):
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
    stage = models.CharField(max_length=400, blank=False, null=True)
    startEndDate = models.CharField(max_length=400, blank=False, null=True)


    def __str__(self):
        return self.employee
