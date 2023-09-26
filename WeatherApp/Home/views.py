from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

# Create your views here.

def Index(request):
    if request.method=='POST':
        city = 'london'
        api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
        response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
        if response.status_code == requests.codes.ok:
            print(response.text)
        else:
            print("Error:", response.status_code, response.text)
    return render(request,"index.html")