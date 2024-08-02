from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import auth


# Create your views here.



def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        age=request.POST['age']
        date=request.POST['date']
        address=request.POST['address']
        image=request.FILES['image']
        data=CustomUser.objects.create_user(first_name=name,email=email,username=username,password=password,age=age,date=date,address=address,image=image)
        data.save()
        return HttpResponse("success")
    else:
        return render(request,'register.html') 


def Login(request):
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect(home)
        else:
            context ={
                'message': "Invalid credentials"
            }
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')
    

def home(request):
    data=CustomUser.objects.get(id=request.user.id)
    return render(request,'home.html',{'data':data})


def logout(request):
    auth.logout(request)
    return redirect(Login)

def edit(request,id):
    data=CustomUser.objects.get(id=id)
    if request.method=='POST':
        data.first_name=request.POST['name']
        data.email=request.POST['email']
        data.age=request.POST['age']
        data.date=request.POST['date']
        data.address=request.POST['address']
        data.image=request.POST['image']
        data.save()
        return redirect(home)
    else:
        return render(request,'edit.html',{'data':data})
