# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors=[]
        name=postData['name']
        username=postData['username']
        password=postData['password']
        password_ver=postData['password_ver']

        if len(name)<0:
            errors.append('Name field is required.')
        elif len(name)<3:
            errors.append('Name should be at least three characters long.')
        if len(username)<0:
            errors.append('Username field is required.')
        elif len(username)<3:
            errors.append('Username must be al least three characters long.')
        if len(password)<0:
            errors.append('Password field is required.')
        elif len(password)<8:
            errors.append('The password must be at least 8 characters long.')
        elif password != password_ver:
            errors.append('Password and password confirmation must match.')
        
        if len(errors)>0:
            return (False, errors)
        else:
            result = self.filter(username=username)
            if len(result)>0:
                errors.append('Username already exists. Please log in.')
                return (False, errors)
            else:
                new_user = self.create(
                    name=name,
                    username=username,
                    password=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                )
                return (True, new_user)

    def log_validation(self, postData):
        errors=[]
        username=postData['lusername']
        password=postData['lpassword']
        if len(username)<0:
            errors.append('The username field is required to log in.')
        elif len(username)<3:
            errors.append('The username is at least three characters long.')
        if len(errors) > 0:
            return (False, errors)
        else:
            login = self.filter(username=username)
            if len(login)>0:
                user = login[0]
                if bcrypt.checkpw(password.encode(), user.password.encode()):
                    return (True, user)
                else:
                    errors.append('Invalid username or password. Please verify and try again.')
                    return (False, errors)
            else:
                errors.append('Invalid username or password. Please verify and try again')
                return (False, errors)

class ItemManager(models.Manager):
    def item_validation(self, postData):
        errors=[]
        newitem=postData['item']
        if len(newitem)<0:
            errors.append('newitem/Product name is required.')
        elif len(newitem)<3:
            errors.append('newitem/Product name should be at least three characters long.')
        
        if len(errors)<0:
            return (False, errors)
        else:
            new_item=self.create(
                item_name=newitem
            )
            return (True, new_item)

class User(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects=UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    item_name=models.CharField(max_length=255)
    users=models.ManyToManyField(User, related_name="wishlisted")
    objects=ItemManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)