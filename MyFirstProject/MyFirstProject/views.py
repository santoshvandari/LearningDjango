from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> Welcome the Home Page</h1>")

def DynamicUrl(request):
    return HttpResponse("<h1> Dynamic URL Page</h1>")
