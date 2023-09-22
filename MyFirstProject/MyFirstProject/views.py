from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome the Home Page</h1>")

def DynamicUrl(request):
    return HttpResponse("<h1> Dynamic URL Page</h1>")

def DynamicContent(request,Data):
    return HttpResponse(f"The Url is: http://127.0.0.1:8000/Dynamic/{Data}")