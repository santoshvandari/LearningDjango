from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def santosh(request):
    senddata={
        'name':'Santosh',
        'age':20,
        'hobby':'Coding',
        'address':'Kathmandu',
        'college':'Kathmandu Engineering College',
    }
    # return HttpResponse("Hello Santosh")
    return JsonResponse(senddata)