"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
import students
from students import views
from django.template import RequestContext
from django.shortcuts import render


# def handler500(request, *args, **argv):
#     response = render('500.html', {}, context_instance=RequestContext(request))
#     response.status_code = 500
#     return response


urlpatterns = [
    # Students urls
    path(r'', students.views.students_list, name='home'),
    path(r'students/add/', students.views.groups_add, name='students_add'),
    re_path(r'^students/(?P<sid>\d+)/edit/$', students.views.students_edit, name='students_edit'),
    re_path(r'^students/(?P<sid>\d+)/delete/$', students.views.students_delete, name='students_delete'),
    # Groups urls
    path(r'groups/', students.views.groups_list, name='groups'),
    path(r'groups/add', students.views.groups_add, name='groups_add'),
    re_path(r'^groups/(?P<sid>\d+)/edit/$', students.views.groups_edit, name='groups_edit'),
    re_path(r'^groups/(?P<sid>\d+)/delete/$', students.views.groups_delete, name='groups_delete'),

    path('admin/', admin.site.urls),
]
