# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from models import User
from django.shortcuts import render, redirect

def index(request):
    try:
        request.session['user_id']
    except KeyError:
        return render(request, 'login_regi/index.html')
    return redirect('/user/dashboard')

def register(request):
    results = User.objects.register_val(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    else:
        user = User.objects.create_user(request.POST)
    request.session['user_id'] = user.id
    return redirect('/user/dashboard')

def login(request):
    results = User.objects.login_val(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request,error)
        return redirect('/')

    request.session['user_id'] = results['user'].id
    messages.success(request, "Logged in!")
    return redirect('/user/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')
