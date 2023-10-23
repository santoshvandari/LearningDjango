from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from API.models import QuotesCollection
from API.serilizers import QuotesCollectionSerializer


# Create your views here.
class QuotesCollectionViewSet(viewsets.ModelViewSet):
    queryset = QuotesCollection.objects.all()
    serializer_class = QuotesCollectionSerializer

def Home(request):
    return HttpResponse("Hello World")
    return render(request,"home.html")