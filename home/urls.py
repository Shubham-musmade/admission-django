from django.contrib import admin
from django.urls import path
from home import views, admission

urlpatterns = [
    path("", views.index, name='index'),#home stands for project app
    path("home/", views.home, name='home'),#this is for another page
    path("about_us/", views.about_us, name='about_us'),
    path("contact/", views.contact, name='contact'),
    path("pri_admission/", admission.pri_admission, name='pri_admission'),
    path("high_admission/", admission.high_admission, name='high_admission'),
    path("reclass/", admission.reclass, name='reclass'),
    path("apointment/", views.apointment, name='apointment'),
    path("login_user", views.login_user, name='login_user'),
    path("sign_up/", views.sign_up, name='sign_up'),
    path("logout",views.logout_user, name="logout"),
]