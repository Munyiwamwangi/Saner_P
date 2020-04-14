from django.db import models
from employee.models import  Employee


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
    Id = models.CharField(primary_key=True, max_length=400)
    approval_status = models.CharField(max_length=400, blank=False, null=True)
    comments = models.CharField(max_length=400, blank=False, null=True)
    coverage_plans = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=False, null=True, related_name='coverage_plans')
    department_team_lead = models.CharField(max_length=400, blank=False, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    employee_s_department = models.CharField(max_length=400, blank=False, null=True)
    HR_approve_cancellation = models.BooleanField(max_length=400, blank=False, null=True)
    leave_approved = models.CharField(max_length=400, blank=False, null=True)
    leave_end_date = models.CharField(max_length=400, blank=False, null=True)
    leave_entitlement_utilization = models.CharField(max_length=400, blank=False, null=True)
    leave_start_date = models.CharField(max_length=400, blank=False, null=True)
    leave_started = models.CharField(max_length=400, blank=False, null=True)
    leave_type = models.CharField(max_length=400, blank=False, null=True)
    line_manager_account = models.ForeignKey(Employee, on_delete=models.SET_NULL, blank=False, null=True, related_name='line_manager_account')
    line_manager_approve_cancellation = models.CharField(max_length=400, blank=False, null=True)
    next_step = models.CharField(max_length=400, blank=False, null=True)
    next_step_due_date = models.CharField(max_length=400, blank=False, null=True)
    no_of_approved_leave_days = models.CharField(max_length=400, blank=False, null=True)
    no_of_leave_days_requested = models.CharField(max_length=400, blank=False, null=True)
    request_from_VFP = models.CharField(max_length=400, blank=False, null=True)
    sick_leave_doc_attached = models.FileField(upload_to='sick_leave_documents', null=True, blank=False)
    stage = models.CharField(max_length=400, blank=False, null=False, default='Open')
    startEndDate = models.CharField(max_length=400, blank=False, null=True)

    def __str__(self):
        return '%s %s %s' % (self.Id, self.employee, self.leave_type)


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

    def __str__(self):
        return self.Decsritption


class Leave_Entitlement_Utilization(models .Model):
    id = models.CharField(primary_key=True, max_length=400)
    Accrued_To_Date_Selected = models.CharField(max_length=300, null=True, blank=True)
    Employee = models.CharField(max_length=300, null=True, blank=True)
    Leave_Days_Accrued = models.CharField(max_length=300, null=True, blank=True)
    Leave_Days_Remaining = models.CharField(max_length=300, null=True, blank=True)
    Leave_Days_Scheduled = models.CharField(max_length=300, null=True, blank=True)
    Leave_Days_Used = models.CharField(max_length=300, null=True, blank=True)
    Leave_Entitlement_Type_Config = models.CharField(max_length=300, null=True, blank=True)
    Leave_Type = models.CharField(max_length=300, null=True, blank=True)
    Leave_Type_Name = models.CharField(max_length=300, null=True, blank=True)
    Leave_Year = models.CharField(max_length=300, null=True, blank=True)
    Total_No_of_Leave_Days = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.Leave_Days_Accrued


class SanergyDepartment(models.Model):
    id = models.CharField(primary_key=True, max_length=400)
    name = models.CharField(max_length = 100, blank=True, null=True)
    approver = models.CharField(max_length=300, null=True, blank=True)
    company = models.CharField(max_length=300, null=True, blank=True)
    department_code = models.CharField(max_length=300, null=True, blank=True)
    department_status = models.CharField(max_length=300, null=True, blank=True)
    team_lead = models.CharField(max_length = 1000, null=True, blank=True)
    team_lead_sf_account = models.CharField(max_length = 1000, null=True, blank=True)

    def __str__(self):
        return self.department_code


class SanergyDepartmentUnit(models.Model):
    id = models.CharField(primary_key=True, max_length=400)
    name = models.CharField(max_length = 100, blank=True, null=True)
    active = models.BooleanField(null=True, blank=True)
    approver = models.CharField(max_length=300, null=True, blank=True)
    department_unit_code = models.CharField(max_length = 100, null=True, blank=True)
    line_manager = models.CharField(max_length=100, null=True, blank=True)
    line_manager_sf_account = models.CharField(max_length=100, null=True, blank=True)
    sanergy_department = models.ForeignKey(SanergyDepartment, on_delete=models.SET_NULL, null=True, blank=True)
    talent_partner_emp_eccount = models.CharField(max_length=100, null=True, blank=True)
    talent_partner = models.CharField(max_length=100, null=True, blank=True)
    team_lead = models.CharField(max_length = 1000, null=True, blank=True)
    team_lead_sf_account = models.CharField(max_length = 1000, null=True, blank=True)
    uit_code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.department_unit_code

    @classmethod
    def fetch_department_units(cls):
        all_department_units = cls.objects.all()
        return all_department_units.department_unit_code