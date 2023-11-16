from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def index(request):


    return render(request,"index.html")

def signin(request):
    return render(request,"signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(username, name,email,password)
    return render(request,"signup.html")

def logout(request):
    pass

def dashboard(request):
    if(User.is_authenticated):
        return render(request,"dashboard.html",{'user':User.first_name})
    else:
        return redirect("/signin")
    