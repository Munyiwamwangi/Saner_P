from django.urls import path
from . import views


urlpatterns = [
    path('', views.employee_details, name='employee_details'),
    path('psqlEmployee', views.psqlEmployeeDetails, name='psqlrecord')
]
