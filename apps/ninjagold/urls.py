from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.ninjagold),
    url(r'^process$', views.process),
]
