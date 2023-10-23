from API.models import QuotesCollection
from rest_framework import serializers


class QuotesCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        id=serializers.ReadOnlyField()
        model = QuotesCollection
        fields = "__all__"