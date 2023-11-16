from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate


# Create your views here.
def index(request):

    return render(request,"index.html")

def signin(request):
    if request.method=='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/dashboard")
        else:
            return render(request,"signin.html")
    return render(request,"signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username,email,password)
        user.first_name = name
        user.save()
        login(request,user)
        return redirect("/dashboard")
    return render(request,"signup.html")

def logout(request):
    if (request.user is not None):
        logout(request)
        return redirect("/")

def dashboard(request):
    if(request.user.is_authenticated):
        return render(request,"dashboard.html",{'user':User.first_name})
    else:
        return redirect("/signin")
    