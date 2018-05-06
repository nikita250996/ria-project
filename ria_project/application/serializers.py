from rest_framework import serializers
from .models import *


class RequestSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField(many=True)

    class Meta:
        model = Request
        fields = '__all__'
        depth = 1

