from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your models here.



class addtask(models.Model):
    name = models.TextField(default="", max_length=30)
    time = models.DateTimeField(default="")
    details = models.TextField(default="", max_length=10)
    status = models.BooleanField(default=False)
