from django.shortcuts import render
from django.shortcuts import render
from django.conf import settings
from instaclone.models import SignUp
from instaclone.forms import SignUPFORM

def signup(request):
	suform=SignUPFORM(request.POST)
	print suform
	print "method",request.method
	if request.method=="GET":
		return render(request,"index.html" ,{})
	elif request.method=="POST":
		suname=request.POST.get("name")
		print "suname",suname
		suuser=request.POST.get("username")
		suemail=request.POST.get("email")
		supass=request.POST.get("password")
		dict={
		"name":suname,
		"username":suuser,
		"email":suemail,
		"password":supass

		}
		return render(request,"make.html" ,dict)

#def signup(request):
