# Create your models here.
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from users.models import CustomUser


class Employee(models.Model):
    Id = models.CharField(primary_key=True,max_length=100, blank=False )
    Employee_First_Name = models.CharField(max_length=100, blank=False, null=True)
    Employee_Last_Name = models.CharField(max_length=100, null=True)
    Employee_Full_Name = models.CharField(max_length=100, blank=False)
    Company_Division = models.CharField(max_length=100, blank=True)
    Employee_Department = models.CharField(max_length=100, blank=True, null=True)
    Sanergy_Department = models.CharField(max_length=100, null=True)
    Sanergy_Department_Unit = models.CharField(max_length=100, null=True)
    Talent_Partner = models.CharField(max_length=100, null = True, blank=True)
    Team_Lead = models.CharField(max_length=100, blank=True, null=True )
    Employee_Active = models.BooleanField(default=True, null=True)
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    HR_Employee_ID = models.EmailField(unique=True, null=True)
    Line_Manager = models.CharField(max_length=100, blank=False, null=True )
    IsDeleted = models.BooleanField(null=True)
    Image = models.FileField(default='default.jpg', upload_to='profile_pics')
    Date_Of_Birth = models.DateField(default=timezone.now)
    Joined_Date = models.DateField(default=timezone.now)
    Phone_Number = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_employee = models.BooleanField(default=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null = True)

    class Meta:
        ordering = ('Employee_Full_Name',)

    def __str__(self):
        return self.Employee_Full_Name