from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name='landing'),
    path('create_custom_user', views.create_custom_user, name='create_custom_user'),
    path('employee_details', views.employee_details, name='employee_details'),
    path('employee_profile', views.employee_profile, name='employee_profile'),
    path('populate_postgres', views.populate_postgres, name='populate_postgres'),
]
