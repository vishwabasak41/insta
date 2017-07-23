from __future__ import unicode_literals

from django.conf import settings

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField(default=None)
	name=models.CharField(max_length=120)
	username=models.CharField(max_length=120)
	password=models.CharField(max_length=40)
	createdon=models.DateTimeField(blank=True,null=True,auto_now_add=True)
	updated=models.DateTimeField(auto_now=True,blank=True,null=True)
	image=models.FileField(blank=True,null=True)

	

	def __unicode__(self):
		return self.name


	def __str__(self):
		return self.name


class login(models.Model):
	username=models.CharField(max_length=120,blank=True,null=True)
	password=models.CharField(max_length=120)
	
	def __unicode__(self):
		return self.username

class upload(models.Model):
	username=models.CharField(max_length=120)
	image=models.FileField(blank=True,null=True)

