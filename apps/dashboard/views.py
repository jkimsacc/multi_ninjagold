# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_regi.models import User
from ..ninjagold.models import Log

def dashboard(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')

    context ={
        'top5': [
            User.objects.all().order_by("-gold")[0],
            User.objects.all().order_by("-gold")[1],
            User.objects.all().order_by("-gold")[2],
            User.objects.all().order_by("-gold")[3],
            User.objects.all().order_by("-gold")[4],
            ]
        }
    return render(request, 'dashboard/dashboard.html', context)

def all_user(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context ={
        'users': User.objects.order_by("-updated_at"),
    }
    return render(request, 'dashboard/all_user.html', context)

def user_page(request, user_id):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context={
        'user': User.objects.get(id = user_id),
        'logs': Log.objects.filter(user_id = user_id)
    }
    return render(request, 'dashboard/user_page.html', context)

# Create your views here.
