from django.urls import path
from . import views


urlpatterns = [
    path('', views.leave_entitlement_types, name='leave_entitlement_types'),
    path('leave_application', views.leave_application, name='leave_application'),
    path('accruals', views.populate_leaveAccruals, name='accruals_leave'),
    path('employee_leave_request', views.employee_leave_request, name='employee_leave_request'),
    path('populate_sanergy_calender', views.populate_sanergy_calender, name='populate_sanergy_calender'),
]
