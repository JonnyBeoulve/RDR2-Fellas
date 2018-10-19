"""rdr2_fellas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from rdr2_fellas import views

# Namespace
app_name = 'rdr2_fellas'

# URL structure
urlpatterns = [
    url(r'^about/$', views.about, name='about'),
    url(r'^partner/$', views.partner, name='partner'),
    url(r'^myprofile/$', views.my_profile, name='myprofile'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^admin/$', admin.site.urls),
    url(r'', views.home, name='home'),
]
