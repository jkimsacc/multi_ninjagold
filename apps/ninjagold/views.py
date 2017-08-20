# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random
from ..login_regi.models import User
from models import Log

def ninjagold(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context ={
        'user': User.objects.get(id=request.session['user_id']),
        'logs': Log.objects.filter(user_id=request.session['user_id']).order_by("-created_at"),
    }
    return render(request, 'ninjagold/ninjagold.html', context)

def process(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    user = User.objects.get(id = request.session['user_id'])
    print request.POST['building']
    if request.POST['building'] == "cave":
        earn = random.randrange(-5, 6)
    elif request.POST['building'] == "castle":
        earn = random.randrange(-10, 11)
    elif request.POST['building'] == "farm":
        earn = random.randrange(-1, 2)

    user.gold += earn
    log = Log.objects.create(
        place = request.POST['building'],
        earn = earn,
        user = user,
    )
    if user.gold > 0:
        user.save()
    else:
        user.delete()
        return redirect('/')


    return redirect('/ninja_gold')
# Create your views here.
