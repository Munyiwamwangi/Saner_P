from django.urls import path
from . import views


urlpatterns = [
    path('', views.leave_types, name='types-leave'),
    path('request', views.request_leave, name='request-leave'),
    path('approve', views.approve_leave, name='approve-leave'),
    
]
