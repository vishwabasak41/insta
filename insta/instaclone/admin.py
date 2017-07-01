from django.contrib import admin
from.forms import  SignUPFORM,Loginform
from .models import SignUp,login

class SUadmin(admin.ModelAdmin):
	list_display=["name","createdon","updated","image"]
	model=SignUp
	form=SignUPFORM



class LoginAdmin(admin.ModelAdmin):
	list_display=["emailog"]
	model=login
	form=Loginform

modes=[SignUp,login] 

admin.site.register(modes)