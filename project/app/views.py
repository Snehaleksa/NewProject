from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import CustomUser

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
    