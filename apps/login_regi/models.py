# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
import datetime
from django.db import models


EMAIL_REGEX = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

class UserManager(models.Manager):
    def register_val(self, post_data):
        results = {'status': True, 'errors': [], 'user': None}
        if len(self.filter(email = post_data['email'])) > 0:
            results['errors'].append('Email already in use')
        if not re.match(EMAIL_REGEX, post_data['email']):
            results['errors'].append('Invalid email format')
        if len(post_data['username']) < 2:
            results['errors'].append('Username need to be more than 2 characters')
        if len(self.filter(username = post_data['username'])) > 0:
            results['errors'].append('Username already taken')
        if len(post_data['password']) < 5:
            results['errors'].append('Your password should be at least 6 letters')
        if post_data['password'] != post_data['confirm_pw']:
            results['errors'].append('Your password does not match')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

    def create_user(self, post_data):
        hashed = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
        user = self.create(
            email = post_data['email'],
            username = post_data['username'],
            password = hashed,
            gold = 200
        )
        return user

    def login_val(self, post_data):
        results = {'status': True, 'errors': [], 'user': None}
        if len(self.filter(email = post_data['email'])) == 0:
            results['errors'].append('Invalid Email or Password')
        else:
            results['user'] = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), results['user'].password.encode()):
                results['errors'].append('Invalid Email or Password')
        if len(results['errors']) > 0:
            results['status'] = False
        return results

class User(models.Model):
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gold = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
