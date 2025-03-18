from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
def homepage ( request ):
    return render(request, "index.html")
def signinpage( request ):
    #return HttpResponse(" <input> ")
    print("You did a"+ request.method)
    if request.method == "POST":
        print( request.POST)
        typedname = request.POST.get("username")
        print("The name you typed is :" + typedname)
        typedPassword = request.POST.get("password")
        print(typedPassword)
        result=authenticate(username= typedname, password= typedPassword)
        if result == None:
            return HttpResponse("You aren't registered with us")
        else:
            login(request, result)
            return redirect("homepage")
            
    
    return render(request, "signin.html")
def signuppage( request ):
    if request.method == "POST":
        print( request.POST)
        typedname = request.POST.get("username")
        print("The name you typed is :" + typedname)
        typedPassword = request.POST.get("password")
        print(typedPassword)
        typedemail = request.POST.get("email-address")
        print("The email you typed is :" + typedemail)
        typedfirstname = request.POST.get("first-name")
        print("The First Name you typed is :" + typedfirstname)
        typedlastname = request.POST.get("last-name")
        print("The Last Name you typed is :" + typedlastname)
        new_password = make_password(typedPassword)
        new_user=User(first_name = typedfirstname, last_name = typedlastname, password = new_password, email = typedemail, username = typedname)  
        new_user.save()
        return redirect("signinpage")   
    return render(request, "signup.html")

def Signout(request):
    logout(request)
    return redirect("signuppage")

def randompage(request):
    return redirect("homepage")
