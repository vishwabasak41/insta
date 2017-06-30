from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from instaclone.models import SignUp,login
from instaclone.forms import SignUPFORM,Loginform

def signup(request):
	suform=SignUPFORM(request.POST)
	print suform
	print "method",request.method
	if request.method=="GET":
		print("inside get")
		return render(request,"index.html" ,{})
	elif request.method=="POST":
		print(suform.is_valid())


		# print("\n\n", request.POST.data, "\n\n")
		print("\n\n", request.POST.get("username"), "\n\n")

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
			suform.save()
			dict={
			"suform":suform,
			"name":suname,
			"username":suuser,
			"email":suemail,
			"password":supass
			}
			return render(request,"make.html" ,dict)

def login_user(request):
	loginform=Loginform(request.POST)
	instance=login.objects.all()
	print "instance",instance
	return render(request,"login.html",{})


