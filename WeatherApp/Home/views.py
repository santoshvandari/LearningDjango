from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def Index(request):
    if request.method=='POST':
        pass
    return render(request,"index.html")