from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    path('request', views.request_leave, name='request-leave'),
    path('approve', views.approve_leave, name='approve-leave'),
=======
    path('', views.request_leave, name='request-leave'),
    path('leave_application', views.leave_application, name='leave_application'),
    path('approve', views.approve_leave, name='approve-leave'),
    path('leave_types', views.leave_types, name='leave_types'),
>>>>>>> fetching bulk employee objects from sf
    path('types', views.leave_types, name='types-leave'),
=======
    path('', views.leave_application, name='leave_application'),
    path('home', views.home, name='home'),
    path('employee_details', views.employee_details, name='employee_details'),
>>>>>>> deserialization complete

]
