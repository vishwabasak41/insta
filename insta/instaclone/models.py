from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField()
	name=models.CharField(max_length=120)
	username=models.CharField(max_length=120)
	password=models.CharField(max_length=40)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class login(models.Model):
	emailog=models.EmailField()
	password=models.CharField(max_length=120)
