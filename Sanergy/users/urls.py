from django.urls import path
from . import views
# from ..leave_management.views import request_leave
from django.views.generic.base import TemplateView
from . import views


urlpatterns = [
    path('reset/done/', views.password_reset_done, name='password_reset_done'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('create_custom_user', views.create_custom_user, name='create_custom_user'),
    path('user_directory/', views.user_directory, name='user_directory'),
]
=======
    path('create_custom_user/', views.create_custom_user, name='create_custom_user'),
    path('user_directory/', views.user_directory, name='user_directory'),
=======
    path('create_custom_user', views.create_custom_user, name='create_custom_user'),
    path('', views.landing, name='landing'),
    path('leave_page', views.request_leave, name='leave'),
    
    
    
>>>>>>> Integrating the login templated

]
>>>>>>> whos is out done, by filtered by  department units
