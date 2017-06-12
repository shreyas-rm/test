from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^login/do', actionLogin, name='users-login-action'),
    url(r'^login', signin, name='users-login'),
    url(r'^logout', signout, name='users-logout'),
    
    url(r'^$', signin, name='users-login'),
]