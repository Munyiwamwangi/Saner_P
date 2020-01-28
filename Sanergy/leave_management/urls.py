from django.urls import path
from . import views


urlpatterns = [
    path('', views.leave_entitlement_types, name='leave_entitlement_types'),
    path('requests', views.request_leave, name='request_leave'),
    path('accruals', views.populate_leaveAccruals, name='accruals_leave'),
    path('employee_leave_request', views.employee_leave_request, name='employee_leave_request'),

]
