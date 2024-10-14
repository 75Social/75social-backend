from rest_framework import serializers
from .models import HelloWorld

class  HelloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HelloWorld
        fields = ('title','description')

        