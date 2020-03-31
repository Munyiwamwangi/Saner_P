from django.urls import path
from . import views


urlpatterns = [
    # path('', views.landing, name='landing'),
    path('employee_directory', views.employee_directory, name='employee_directory'),
    path('user_directory', views.user_directory, name='user_directory'),
    path('employee_profile', views.employee_profile, name='employee_profile'),
    path('populate_postgres', views.populate_postgres, name='populate_postgres'),
    path('refresh_employees', views.refresh_employees, name='refresh_employees'),
]
