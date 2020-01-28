from django.contrib.auth.models import User
from django.db import models


class LeaveType(models.Model):
    LEAVE_CHOICES = (
        ('SICK_LEAVE', 'SICK_LEAVE'),

        ('STUDY_LEAVE', 'STUDY_LEAVE'),

        ('EXAM_LEAVE', 'EXAM_LEAVE'),

        ('MATERNITY_LEAVE', 'MATERNITY_LEAVE'),

        ('PATERNITY_LEAVE', 'PATERNITY_LEAVE'),

        ('ANNUAL_LEAVE', 'ANNUAL_LEAVE'),

        ('COMPASSIONATE_LEAVE', 'COMPASSIONATE_LEAVE'),

    )

    Leave_Types = models.CharField(max_length=20, choices=LEAVE_CHOICES, default='annual')

    def __str__(self):
        return self.Leave_Types


class LeaveClassDetails(models.Model):
    Approved = 0

    Pending = 1

    Declined = 2

    PendingCancellation = 3

    LeaveStatus = (
        (Approved, 'Approved'),

        (Pending, 'Pending'),

        (Declined, 'Declined'),

        (PendingCancellation, 'PendingCancellation'),
    )

    Leave_Id = models.AutoField(primary_key=True)
    Leave_Type = models.CharField(max_length=1, choices=LeaveStatus, )
    Begin_Date = models.DateField(help_text='Leave begin date')
    End_Date = models.DateField(help_text='Leave end date')
    Requested_Days = models.IntegerField(default=0, help_text='Total no of requested leave days')
    Leave_Status = models.IntegerField(choices=LeaveStatus, default=1)
    Comments = models.CharField(max_length=500, null=True)
    Coverage_Plans = models.ForeignKey(User, on_delete=models.DO_NOTHING, max_length=50, )
    Leave_Attachments = models.FileField(upload_to='leave_management/media/leave_documents', unique=False, blank=False)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    Submitted_Date = models.DateTimeField(auto_now_add=True, )

    class Meta:
        ordering = ('-Leave_Id',)

    def __str__(self):
        return '%s %s' % (self.Leave_Id, self.Comments)


class LeaveModels(models.Model):
    employee = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.employee
