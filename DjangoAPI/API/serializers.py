from  API.models import PersonalInformation 
from rest_framework import serializers


class PersonalInformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        
        model = PersonalInformation
        fields = ['personalId', 'name', 'address', 'description', 'date']