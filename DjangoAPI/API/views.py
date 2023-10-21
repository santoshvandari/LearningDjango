from django.shortcuts import render,HttpResponse
from API.models import PersonalInformation
from rest_framework import viewsets
from API.serializers import PersonalInformationSerializer

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Hello Universe</h1>")

class PersonalInformationViewset(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer
