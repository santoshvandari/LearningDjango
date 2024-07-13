from django.shortcuts import render,HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("Task is Running")