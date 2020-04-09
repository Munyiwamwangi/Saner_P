# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.urls import reverse
from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
# from leave_management.models import SanergyDepartment, SanergyDepartmentUnit

from users.models import CustomUser


class Employee(models.Model):
    Id = models.CharField(primary_key=True,max_length=100, blank=False)
    Employee_First_Name = models.CharField(max_length=100, blank=False, null=True)
    Employee_Last_Name = models.CharField(max_length=100, null=True)
    Employee_Middle_Name = models.CharField(max_length=100, null=True)
    Employee_Full_Name = models.CharField(max_length=100, blank=False)
    Company_Division = models.CharField(max_length=100, blank=True)
    Sanergy_Department = models.CharField(max_length=100, null=True)
    Sanergy_Department_Unit = models.CharField(max_length=100, null=True)
    Employee_Active = models.BooleanField(default=True, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    IsDeleted = models.BooleanField(null=True)
    Image = models.FileField(default='default.jpg', upload_to='profile_pics')
    Date_Of_Birth = models.DateField(default=timezone.now)
    Joined_Date = models.DateField(default=timezone.now)
    is_staff = models.BooleanField(default=False, null=True)
    is_employee = models.BooleanField(default=True, null=True)
    HR_Employee_ID = models.CharField(unique=True, max_length=100, null=True)
    Leave_Group = models.CharField(unique=False, max_length=100, null=True)
    Employee_Role = models.CharField(unique=False, max_length=100, null=True)
    Primary_Phone = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null = True, blank=True)
    
    Team_Lead = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, null=True, related_name='team_lead')
    Line_Manager = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, null=True, related_name='line_manager')
    Talent_Partner = models.ForeignKey('Employee', on_delete=models.DO_NOTHING, null=True, related_name='talent_partner')

    class Meta:
        ordering = ('Employee_First_Name',)

    def __str__(self):
        return self.Employee_Full_Name

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})
