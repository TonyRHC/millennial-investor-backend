from rest_framework import serializers
from .models import *

class HeadlinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headliner
        fields = ('pk', 'keyword', 'creationDate')