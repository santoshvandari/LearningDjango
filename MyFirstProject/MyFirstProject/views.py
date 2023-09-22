from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def dynamic(request,data):
    return HttpResponse(data)
    # datas={
    #     'value':data
    # }
    # return render(request,"other.html",datas)

# def DynamicUrl(request):
#     return HttpResponse("<h1> Dynamic URL Page</h1>")

# def DynamicContent(request,data):
#     Data=data
#     return HttpResponse(f"The Url is: <b>http://127.0.0.1:8000/Dynamic/{Data}</b>")