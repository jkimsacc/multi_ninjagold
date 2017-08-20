# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
import datetime
from ..login_regi.models import User
from django.db import models

# Create your models here.
class Log(models.Model):
    place = models.CharField(max_length=100)
    earn = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "by")
