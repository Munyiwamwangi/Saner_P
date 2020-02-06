from django.urls import path
from . import views


urlpatterns = [
    path('', views.leave_entitlement_types, name='leave_entitlement_types'),
    path('request', views.request_leave, name='request_leave'),
    path('approve', views.approve_leave, name='approve_leave'),
    
]
