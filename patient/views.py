from django.shortcuts import render,redirect
from .models import patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def pati(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        Email = request.POST['Email']
        address = request.POST['address']
        password = request.POST['password']
        Confirm_password = request.POST["Confirm_password"]
        image = request.POST["image"]
        if ((len(name)!=0) & (len(Email)!=0) &(len(password)) &(len(Confirm_password)) & (password==Confirm_password)):
            new_patient = patient(name=name,username=username, Email=Email,address=address, password=password,image= image)
            new_patient.save()
            user = User.objects.create_user(username,Email, password)
            user.save()
            return redirect("/patient/")
        else:
            # Add an error message for invalid login
            return render(request, 'psignup.html', {'error_message': 'Please enter valid detail'})
        

        #new_doctor = doctor(name=name, phone_number=phone_number, Email=email, password=password)
        #new_doctor.save()
        #user = User.objects.create_user(username,  password)
        #user.save()
        #return redirect("/sign/")

    return render(request, 'psignup.html')
def pftech(request):
    if request.method == "POST":
        username = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username = username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/patient/pwelcome")
        else:
            # Add an error message for invalid login
            return render(request, 'psignin.html', {'error_message': 'Invalid username or password'})

    return render(request,"psignin.html")
def pwelcome(request):
    return render(request,'pwelcome.html')



