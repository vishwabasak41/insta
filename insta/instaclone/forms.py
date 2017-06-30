from django import forms
from .models import SignUp



class SignUPFORM(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['email','username','name','password']
		#we can use exclude to exclude fields
		widgets = {
	        'password': forms.PasswordInput(),
	    }
		