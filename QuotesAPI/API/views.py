from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from API.models import QuotesCollection
from API.serilizers import QuotesCollectionSerializer
import random


# Create your views here.
class QuotesCollectionViewSet(viewsets.ModelViewSet):
    # queryset = QuotesCollection.objects.all()
    # datalength = QuotesCollection.objects.all().count()
    # generate the random number
    # random_index = random.randint(0, datalength - 1)
    # random_index=0
    queryset=QuotesCollection.objects.all()
    # print(queryset.size)
    
    serializer_class = QuotesCollectionSerializer

def Home(request):
    return HttpResponse("Hello World")
    return render(request,"home.html")