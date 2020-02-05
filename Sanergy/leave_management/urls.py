from django.urls import path
from . import views


urlpatterns = [
    path('', views.Leave_Entitlement_Types, name='Leave_Entitlement_Types'),
    path('request', views.request_leave, name='request_leave'),
    path('approve', views.approve_leave, name='approve_leave'),
    
]
