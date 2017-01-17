"""fleet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'vehicles'


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.vehs_list, name='list'),
    url(r'^(?P<vehmaster_Veh_Reg_No>)/$', views.detail, name='detail'),
    url(r'^(AB23 XYZ)/$', views.detail, name='detail'),


]


'''
    #url(r'^vehicles/', include(fleet.urls)),
    #url(r'^(AB23 XYZ)/$', views.detail, name='detail'),

    #url(r'^({{ vehmaster.Veh_Reg_No }})/$', views.detail, name='detail'),    
    #url(r'^(?P<vehicles_Veh_Reg_No>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<vehmaster_id>)$', views.detail, name='detail'),
    #url(r'^/2/$', views.detail, name='detail'),

    #url(r'^$', views.RepairView.as_view(), name='repair'),

    #url(r'^(?P<vehmaster_id>[0-9]+)/$', views.detail, name='detail'),
'''
