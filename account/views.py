from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as ulogin
from django.contrib.auth import logout as ulogout
from .form_validate import check_mobile, check_name, check_email
from django.contrib import messages
from .models import User


# Create your views here.

def Signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            sname = request.POST.get("sname")
            email = request.POST.get("email")
            mobile = request.POST.get("mobile")
            password1 = request.POST.get("password1")
            password2 = request.POST.get("password2")
            if sname and email and mobile and password1 and password2:
                if password1 == password2:
                    if check_mobile(mobile):
                        if check_email(email):
                            if check_name(sname):
                                check_unique_mail = User.objects.filter(email=email)
                                if not check_unique_mail:
                                    User.objects.create_user(email, password1, sname, mobile)
                                    messages.error(request, "Account has been created!")
                                else:
                                    messages.error(request, "Register with another email id!")
                            else:
                                messages.error(request, "Name should be alphabetical form")

                        else:
                            messages.error(request, "Enter a valid email id!")
                    else:
                        messages.error(request, "Mobile number should be 10 digit and digit form")
                else:
                    messages.error(request, "password does not match!")
            else:
                messages.error(request, "fill required field!!")

        return render(request, 'signup.html')

    else:
     return redirect("/library")




def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            if email and password:
                if check_email(email):
                    authenticate_user = authenticate(username=email, password=password)
                    if authenticate_user:
                        ulogin(request, authenticate_user)
                        return redirect("/library")
                    else:
                        messages.error(request, "invalid creadientials!")
                else:
                    messages.error(request, "enter a valid email!!")
            else:
                messages.error(request, "Fill required all fields!")
        return render(request, 'login.html')

    else:
        return redirect("/library")




def logout(request):
    if request.user.is_authenticated:
        ulogout(request)
        return redirect("/login")
    else:
        redirect("/library")
