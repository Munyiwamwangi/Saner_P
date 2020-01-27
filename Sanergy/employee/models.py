from django.db import models
from django.utils import timezone

# Create your models here.


class Employee(models.Model):
    Employee_First_Name = models.CharField(max_length=100,)
    Employee_Last_Name = models.CharField(max_length=100)
    Company_Division = models.CharField(max_length=100)
    Sanergy_Department = models.CharField(max_length=100)
    Sanergy_Department_Unit = models.CharField(max_length=100)
    Employee_Name = models.CharField(max_length=100)
    Work_Email = models.CharField(max_length=100)
   
