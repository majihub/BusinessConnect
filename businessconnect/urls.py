"""
URL configuration for businessconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from buisnessapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('contact',views.contacts,name='contact'),
    path('logout',views.logout,name='logout'),
    path('businessproposal',views.busi_propo,name='businessproposal'),
    path('viewproposal',views.view_propo,name='viewproposal'),
    path('allproposals',views.allproposal,name='allproposals'),
    path('updateproposal/<int:id>',views.update_bproposal,name='updateproposal'),
    path('myprofile',views.my_profile,name="myprofile"),
    path('profileupdate/<int:id>',views.update_profile,name="profileupdate"),
    path('addquery',views.query_func,name="addquery"),
    path('viewquery/',views.viewquery,name="viewquery"),
    path('applyjobs/<int:id>',views.applyjob,name="applyjob"),
    path('viewjobs',views.viewjobs,name='viewjobs'),
    path('investorinterest/<int:id>',views.investorinterest,name='investorinterest'),
    path('interests',views.viewinterest,name='interests'),
]
