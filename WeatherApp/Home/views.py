from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

# Create your views here.

def Index(request):
    if request.method=='POST':
        request.POST
        city =   request.POST.get("city")
        api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
        try: 
            response = requests.get(api_url, headers={'X-Api-Key': 'U3b+x3/lun8o6+Mm0qYWQw==H7yIc2DshurjNdq7'})
            if response.status_code == requests.codes.ok:
                response=response.json()
                return render(request,"index.html",response)
            else:
                return render(request,"index.html",{'code':response.status_code})
        except:
            return render(request,"index.html",{"error":True})

    return render(request,"index.html")
