from . import views
from django.urls import path

urlpatterns = [
    path ('signup',views.signup, name = 'signup'),
    path ('login',views.login, name = 'login'),
    path ('courseinfo',views.courseinfo, name = 'courseinfo'),
    path ('header',views.header, name = 'header'),
    path ('forgetpass',views.forgetpass, name = 'forgetpass'),



]