"""Sanergy URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView
from users import views


from employee import urls
from users import views as user_views

urlpatterns = [
    path('', views.home, name='login'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('leave/', include('leave_management.urls')),
    path('employee/', include('employee.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.password_reset_done, name="Reset_done"),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)