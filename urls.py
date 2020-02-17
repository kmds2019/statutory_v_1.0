"""MYSITE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from litigation.views import current_datetime
from litigation.views import display_master_list,master_create

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('now/', current_datetime),
    path('litigation/display_master_list', display_master_list),
    path('litigation/', display_master_list),
    path('litigation/add_master',master_create,name='master_create'),
]
