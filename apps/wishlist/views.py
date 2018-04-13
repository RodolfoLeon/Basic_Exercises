# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime

from .models import *

# Create your views here.

def index(request):
    return render(request, 'wishlist/index.html')

def create(request):
    validation = User.objects.reg_validation(request.POST)
    if validation[0]:
        request.session['user_id'] = validation[1].id
        request.session['user_name'] = validation[1].name
        return redirect ('/dashboard')
    else:
        for error in validation[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect ('/')

def login(request):
    validation = User.objects.log_validation(request.POST)
    if validation[0]:
        request.session['user_id'] = validation[1].id
        request.session['user_name'] = validation[1].name
        return redirect ('/dashboard')
    else:
        for error in validation[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect ('/')

def dashboard(request):
    # id=request.session['user_id']
    # info = User.objects.get(id=id).wishlisted.all()
    # context = {
    #     'info':info
    # }
    return render(request, "wishlist/dashboard.html")

def logout(request):
    request.session.flush()
    return redirect('/')

def additem(request):
    return render(request, "wishlist/create.html")

def createitem(request):
    item_validation = Item.objects.item_validation(request.POST)
    if item_validation[0]:
        return redirect ('/dashboard')
    else:
        for error in item_validation[1]:
            messages.add_message(request, messages.INFO, error)
        return redirect ('/')

def iteminfo(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item':item
    }
    return render(request, 'wishlist/wishitem.html', context)