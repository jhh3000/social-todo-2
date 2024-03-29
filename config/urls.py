"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from users.views import home, web_login, web_logout, register
from tasks.views import dashboard, create, delete, toggle

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^user/login', web_login, name='login'),
    url(r'^user/logout', web_logout, name='logout'),
    url(r'^user/register', register, name='register'),
    url(r'^task/$', dashboard, name='dashboard'),
    url(r'^task/create', create, name='task_create'),
    url(r'^task/delete/([0-9]+)/', delete, name='task_delete'),
    url(r'^task/toggle/([0-9]+)/', toggle, name='task_toggle'),
]
