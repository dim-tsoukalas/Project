"""class_manager URL Configuration

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
from django.urls import path

import users.views
import mainpage.views
import staff.views

urlpatterns = [
    path("", mainpage.views.home, name="home"),
    path("signin", users.views.signin, name="signin"),
    path("signout", users.views.signout, name="signout"),
    path("signup", users.views.signup, name="signup"),
    path("signup/student", users.views.signup_student, name="signup_student"),
    path("signup/teacher", users.views.signup_teacher, name="signup_teacher"),
    # Users
    path("users", users.views.users, name="users"),
    path("users/<int:uid>", users.views.user),
    path("users/<int:uid>/update", users.views.user_update),
    # Superuser
    path("superuser", staff.views.superuser, name="superuser"),
    path(
        "superuser/departments",
        staff.views.superuser_departments,
        name="superuser_departments",
    ),
    path(
        "superuser/departments/add",
        staff.views.superuser_departments_add,
        name="superuser_departments_add",
    ),
]
