from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from instaclone.models import SignUp,login
from django.http import HttpResponse
from instaclone.forms import SignUPFORM,Loginform
from django.contrib.auth.hashers import make_password, check_password
from vish import upload_func
from django.contrib.auth.models import User
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

def signup(request):
	suform=SignUPFORM(request.POST or None,request.FILES or None)
	print suform
	print "method",request.method
	if request.method=="GET":
		print("inside get")
		return render(request,"index.html" ,{})
	elif request.method=="POST":
		print suform.is_valid()
		print request.FILES
		if suform.is_valid():
			print("form is valid!")
			suname=request.POST.get("name")
			print "suname",suname
			suuser=request.POST.get("username")
			print "suuser",suuser
			suemail=request.POST.get("email")
			print "suemail",suemail
			supass=request.POST.get("password")
			print "supass",supass
			suimage=request.FILES.get("image")
			print "suimage is",suimage
			suform.save()
			image_name=suimage.name
			name_string=str(image_name)
			print type(name_string)
			upload_func(name_string)

			

			user = User.objects.create_user(suuser,suemail,supass)
			supass=user.set_password(supass)
			user.save()
			dic={
			"suform":suform,
			"name":suname,
			"username":suuser,
			"email":suemail,
			"password":supass,
			"image":suimage,
			"logged_in":"SignedIn"

			}
			return render(request,"make.html" ,dic)

def login_user(request):
	loginform=Loginform(request.POST)

	if request.method=="GET":
		return render(request,"login.html",{})
	#instance=login.objects.filter(id=id)
	#print "instance",instance
	#if request.user.is_authenticated():
	elif request.method=="POST":	
		if True:
			username=request.POST.get("username")
			print "username",username
			password=request.POST.get("password")
			print "password",password
			loginform.save()
			if loginform.is_valid():

				user=authenticate(username=username,password=password)
				print user
				if not user:
					return HttpResponse("not valid account")
				else:
					return HttpResponse("invalid")


                    # token = SessionToken(user=user)
                    # token.create_token()
                    # token.save()
                    # response = redirect('feed/')
                    # response.set_cookie(key='session_token', value=token.session_token)
                    # return response
			# 	else:
		 # 			return HttpResponse("not valid account")
		 # 	else:
		 # 		return HttpResponse("invalid")
	 	# else:
		 # 	return HttpResponse("NOT TRUE")


		d={

			"loginform":loginform,
			"username":username,
			"password":password,
			"logged_in":"LOGGEDin"
		}
	return render(request,"login.html",d)


#def logged_in(request):
#	if request.user.is_autheticated():
#			q



