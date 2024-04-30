from django.shortcuts import render,redirect
from .models import doctor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        Email = request.POST['Email']
        address = request.POST['address']
        password = request.POST['password']
        Confirm_password = request.POST["Confirm_password"]
        image = request.POST["image"]
        if ((len(name)!=0) & (len(Email)!=0) &(len(password)) &(len(Confirm_password)) & (password==Confirm_password)):
            new_doctor = doctor(name=name,username=username, Email=Email,address=address, password=password,image= image)
            new_doctor.save()
            user = User.objects.create_user(username,Email, password)
            user.save()
            return redirect("/doctor/")
        else:
            # Add an error message for invalid login
            return render(request, 'signup.html', {'error_message': 'Please enter valid detail'})
        

        #new_doctor = doctor(name=name, phone_number=phone_number, Email=email, password=password)
        #new_doctor.save()
        #user = User.objects.create_user(username,  password)
        #user.save()
        #return redirect("/sign/")

    return render(request, 'signup.html')
def ftech(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/doctor/welcome")
        else:
            # Add an error message for invalid login
            return render(request, 'signin.html', {'error_message': 'Invalid username or password'})

    return render(request,"signin.html")
def welcome(request):
    return render(request,'welcome.html')



