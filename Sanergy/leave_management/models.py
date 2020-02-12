from django.db import models

from employee.models import Employee


class Leave_Entitlement_Type(models.Model):
    Id = models.CharField(primary_key=True, max_length=50)
    Name = models.CharField(max_length=50, blank=False)
    Leave_Type = models.CharField(max_length=50, blank=False)
    Leave_Group = models.CharField(max_length=50, blank=False)
