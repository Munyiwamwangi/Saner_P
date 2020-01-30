from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('employee_details', views.employee_details, name='employee_details'),
    path('employee_profile', views.employee_profile, name='employee_profile'),
    path('populate_postgres', views.populate_postgres, name='populate_postgres'),
    path('psqlEmployee', views.psqlEmployeeDetails, name='psqlrecord'),
]
