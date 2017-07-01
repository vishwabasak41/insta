from django.contrib import admin
from.forms import  SignUPFORM
from .models import SignUp

class SUadmin(admin.ModelAdmin):
	list_display=["name","createdon","updated"]
	class Meta:
		model=SignUp
		form=SignUPFORM


admin.site.register(SignUp,SUadmin) 