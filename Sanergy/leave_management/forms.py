from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import EmployeeLeaveRequest, Leave_Entitlement_Type

leave_choices = [
    
    ('annual leave','Annual leave'),
    ('compassion leave','Compassion leave'),
    ('maternity leave','Maternity leave'),
    ('Paternity leave', 'Paternity leave'),
    ('study leave', 'Study leave'),
  ]

class LeaveApplicationForm(forms.ModelForm):

    class Meta:
        model= EmployeeLeaveRequest
        widgets = {
           'leave_start_date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'leave_end_date':forms.DateTimeInput(attrs={ 'class':
               'datetime-input'}),
            'Leave_Type':forms.Select(choices=leave_choices)
        }

        fields=['leave_type','leave_start_date','leave_end_date','coverage_plans',]
