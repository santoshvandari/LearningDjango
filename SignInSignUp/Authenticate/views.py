from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def index(request):
    if(request.user.is_authenticated):
        return render(request,"dashboard.html",{'user':request.user.first_name})
    return render(request,"index.html")

def signin(request):
    if(request.user.is_authenticated):
        return render(request,"dashboard.html",{'user':request.user.first_name})
     
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print("user is authenticated")
            login(request,user)
            return redirect("/dashboard")
        else:
            return render(request,"signin.html")
    return render(request,"signin.html")

def signup(request):
    if(request.user.is_authenticated):
        return render(request,"dashboard.html",{'user':request.user.first_name})
     
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if(User.objects.filter(username=username)):
            return render(request, "signup.html",{'username':"Username already Taken!!"})
        if(User.objects.filter(email=email)):
            return render(request, "signup.html",{'email':"Email already Taken!!"})
        user = User.objects.create_user(username,email,password)
        user.first_name = name
        user.save()
        print("user Created")
        login(request,user)
        return redirect("/dashboard")
    return render(request,"signup.html")

def logoutUser(request):
    if (request.user is not None):
        logout(request)
        print("user Logout")
        return redirect("/")
    else:
        return redirect("/dashboard")

def dashboard(request):
    if(request.user.is_authenticated):
        return render(request,"dashboard.html",{'user':request.user.first_name})
    else:
        return redirect("/signin")
    