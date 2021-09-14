"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from bug import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.home_view, name='homepage'),
    path('bug/<int:id>/', views.bug_view, name='bug'),
    path('user/<int:id>/', views.user_view, name='user'),
    path('addbug/', views.addbug_view, name='addbug'),
    path('assigntome/<int:id>/', views.assigntome_view, name='assigntome'),
    path('markdone/<int:id>/', views.markdone_view, name='markdone'),
    path('markinvalid/<int:id>/', views.markinvalid_view, name='markinvalid'),
    path('editbug/<int:id>/', views.editbug_view, name='editbug'),
]