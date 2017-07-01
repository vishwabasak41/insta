from django import forms
from .models import SignUp,login



class SignUPFORM(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['email','username','name','password',"image"]
		#we can use exclude to exclude fields
		widgets = {
	        'password': forms.PasswordInput(),
	    }
		


class Loginform(forms.ModelForm):
	class Meta:
		model=login
		fields='__all__'

