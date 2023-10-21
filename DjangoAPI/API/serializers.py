# from  API.models import PersonalInformation
from API.models import StudentInformation
from rest_framework import serializers


# class PersonalInformationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
        
#         model = PersonalInformation
#         fields = ['personalId', 'name', 'address', 'description', 'date']


class StudentSerilizers(serializers.HyperlinkedModelSerializer):
    studentId=serializers.ReadOnlyField()
    class Meta:
        model=StudentInformation
        fields="__all__"