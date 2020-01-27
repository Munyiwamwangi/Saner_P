from django.urls import path
from . import views


urlpatterns = [
    path('employee', views.employeeDetails, name='employee-record'),
    path('psqlEmployee', views.psqlEmployeeDetails, name='psqlrecord')
]
