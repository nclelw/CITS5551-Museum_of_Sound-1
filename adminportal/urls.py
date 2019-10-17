"""adminportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import include, url
from chatbot.views import fbBotView
# from . import settings

from django.contrib.auth import views



admin.site.site_header = "MoS Admin"
admin.site.site_title = "Museum of Sound Admin Portal"
admin.site.index_title = "Welcome to the Museum of Sound Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    url('chatbot', fbBotView.as_view()),
    path('', include('frontend.urls')),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
