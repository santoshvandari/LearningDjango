from django.shortcuts import render
from Home.consumers import StudentInfo

# Create your views here.


async def home(request):
    return render(request, 'home.html')
