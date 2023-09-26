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
            response=response.json()
            print(response)
            # print(response['temp'])
            # {'cloud_pct': 75, 'temp': 22, 'feels_like': 23, 'humidity': 88, 'min_temp': 22, 'max_temp': 22, 'wind_speed': 2.06, 'wind_degrees': 200, 'sunrise': 1695686921, 'sunset': 1695730313}
            # data=response
            return render(request,"index.html",response)
        else:
            print("Error:", response.status_code, response.text)
    return render(request,"index.html")
