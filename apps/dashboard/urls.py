from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^dashboard', views.dashboard),
    url(r'^all', views.all_user),
    url(r'^(?P<user_id>\d+)', views.user_page)
]
