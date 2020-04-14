from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('search', views.search, name='search'),
    path('employee_directory', views.employee_directory, name='employee_directory'),
    path('employee_profile/<str:Id>/', views.employee_profile, name='employee_profile'),
    path('populate_postgres', views.populate_postgres, name='populate_postgres'),
    path('refresh_employees', views.refresh_employees, name='refresh_employees'),

]
