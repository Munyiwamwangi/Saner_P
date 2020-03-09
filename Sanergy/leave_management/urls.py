from django.urls import path
from . import views


urlpatterns = [
    path('', views.leave_entitlement_types, name='leave_entitlement_types'),
    path('leave_application', views.leave_application, name='leave_application'),
    path('accruals', views.populate_leaveAccruals, name='accruals_leave'),
    path('leave_entitlement_types', views.leave_entitlement_types, name='leave_entitlement_types'),
    path('populate_employee_leave_request', views.populate_employee_leave_request, name='populate_employee_leave_request'),
    path('populate_sanergy_calender', views.populate_sanergy_calender, name='populate_sanergy_calender'),
    path('refresh_sanergy_calender', views.refresh_sanergy_calender, name='refresh_sanergy_calender'),
    path('post_leave_to_salesforce', views.post_leave_to_salesforce, name='post_leave_to_salesforce'),
    path('request_leave', views.request_leave, name='request_leave'),
    path('leave_page', views.request_leave, name='leave'),
    path('request_leave_data', views.request_leave_data, name='request_leave_data'),
    path('entitlement', views.entitlement_utilization, name='entitlement'),
<<<<<<< HEAD
    path('individual_leave_history', views.individual_leave_history, name='individual_leave_history'),
=======
   
>>>>>>> Integrating the login templated
     

]
