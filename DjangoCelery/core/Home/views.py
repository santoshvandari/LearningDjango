from django.shortcuts import render,HttpResponse
from Home.task import WaitingTime

# Create your views here.
def Home(request):
    WaitingTime.delay()
    return HttpResponse("Task is Running")

