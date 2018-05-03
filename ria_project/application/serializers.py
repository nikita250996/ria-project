from rest_framework import serializers
from .models import *


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
