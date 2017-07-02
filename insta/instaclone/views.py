from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from instaclone.models import SignUp,login
from instaclone.forms import SignUPFORM,Loginform

def signup(request):
	suform=SignUPFORM(request.POST or None,request.FILES or None)
	print suform
	print "method",request.method
	if request.method=="GET":
		print("inside get")
		return render(request,"index.html" ,{})
	elif request.method=="POST":
		print suform.is_valid()
		if True:
			print("form is valid!")
			suname=request.POST.get("name")
			print "suname",suname
			suuser=request.POST.get("username")
			print "suuser",suuser
			suemail=request.POST.get("email")
			print "suemail",suemail
			supass=request.POST.get("password")
			print "supass",supass
			suimage=request.POST.get("image")
			print "suimage is",suimage
			suform.save()
			dic={
			"suform":suform,
			"name":suname,
			"username":suuser,
			"email":suemail,
			"password":supass,
			"image":suimage,
			"logged in":"lSigned In"

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
			emailog=request.POST.get("emailog")
			print "emailog",emailog
			password=request.POST.get("password")
			print "password",password

			d={
				"loginform":loginform,
				"emailog":emailog,
				"password":password,
				"logged in":"logged in"
			}
		return render(request,"login.html",d)




