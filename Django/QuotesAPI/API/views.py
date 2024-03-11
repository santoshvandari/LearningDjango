from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from API.models import QuotesCollection
from API.serilizers import QuotesCollectionSerializer
import random


# Create your views here.
class QuotesCollectionViewSet(viewsets.ModelViewSet):
    serializer_class = QuotesCollectionSerializer
    # queryset=QuotesCollection.objects.all()
    def get_queryset(self):
        data_length = QuotesCollection.objects.count()
        random_id = random.randint(1, data_length)
        random_record = QuotesCollection.objects.filter(id=random_id)
        return random_record

def Home(request):
    # return HttpResponse("Hello World")
    return render(request,"index.html")