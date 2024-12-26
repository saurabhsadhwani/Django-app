from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'index.html')
def loggedin(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    return render(request,'loggedin.html')
def loginuser(request):
    if request.method=='POST':
        #check if user is authenticated 
        Username=request.POST.get("Username")
        password=request.POST.get("password")
        user=authenticate(username=Username,password=password)
        if user is not None:
            login(request, user)
            return redirect("/loggedin")
            
        else:
            messages.success(request,"Invalid Credentials !!")
            return render(request,'login.html')
        
    return render(request,'login.html')
def logoutuser(request):
    logout(request)
    print("logged out")
    return redirect("/")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def products(request):
    return render(request,'products.html')
    # return HttpResponse("This is products page")
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request,"Form submitted !!")
    return render(request,'contact.html')
    # return HttpResponse("This is contact page")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("This is services page")