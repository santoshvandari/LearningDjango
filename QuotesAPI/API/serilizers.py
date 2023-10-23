from API.models import QuotesCollection
from rest_framework import serializers


class QuotesCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        # id=serializers.ReadOnlyField()
        model = QuotesCollection
        fields = ['quotes', 'author']
    def validate(self, data):
        # Add your custom validation logic here to prevent duplicates
        # For example, check if the data already exists in the database
        if QuotesCollection.objects.filter(quotes=data['quotes']).exists():
            raise serializers.ValidationError("This data already exists.")
        else: 
            return data