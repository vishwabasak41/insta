from django import forms
from .models import SignUp,login,upload


class SignUPFORM(forms.ModelForm):
	class Meta:
		model=SignUp
		fields='__all__'
		#we can use exclude to exclude fields
		widgets = {
	        'password': forms.PasswordInput,
	    }


class Loginform(forms.ModelForm):
	class Meta:
		model=login
		fields='__all__'

class Upload(forms.ModelForm):
	class Meta:
		models=upload
		firlds='__all__'
