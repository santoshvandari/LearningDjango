from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

# Create your views here.

def Index(request):
    if request.method=='POST':
        city = 'Kathmandu'
        api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
        response = requests.get(api_url, headers={'X-Api-Key': 'U3b+x3/lun8o6+Mm0qYWQw==H7yIc2DshurjNdq7'})
        if response.status_code == requests.codes.ok:
            print(response)
            # data=[

            # ]
            # return render(request,"index.html",response.text)
        else:
            print("Error:", response.status_code, response.text)
    return render(request,"index.html")
