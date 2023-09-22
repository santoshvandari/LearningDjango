from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def dynamic(request,url):
    # return HttpResponse(url)
    datas={
        'value': url,
        'language':["Java","C++","Python","JavaScript"],
        "info":[
            {"name":"Santosh Bhandari","Address":"Birtamode"},
            {"name":"Manoj Oli","Address":"Surunga"}
        ]
    }
    return render(request,"dynamic.html",datas)

# def DynamicUrl(request):
#     return HttpResponse("<h1> Dynamic URL Page</h1>")

# def DynamicContent(request,data):
#     Data=data
#     return HttpResponse(f"The Url is: <b>http://127.0.0.1:8000/Dynamic/{Data}</b>")