from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def loop(request):
    # return HttpResponse(url)
    data={
        'language':["Java","C++","Python","JavaScript"],
        "info":[
            {"name":"Santosh Bhandari","Address":"Birtamode"},
            {"name":"Manoj Oli","Address":"Surunga"}
        ]
    }
    return render(request,"loop.html",data)

# def DynamicUrl(request):
#     return HttpResponse("<h1> Dynamic URL Page</h1>")

# def DynamicContent(request,data):
#     Data=data
#     return HttpResponse(f"The Url is: <b>http://127.0.0.1:8000/Dynamic/{Data}</b>")



def ifelse(request):
    return render(request,"ifelse.html")