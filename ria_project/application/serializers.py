from rest_framework import serializers
from .models import *


class RequestSerializer(serializers.ModelSerializer):
    countries = serializers.StringRelatedField(many=True)
    owners = serializers.StringRelatedField(many=True)
    creators = serializers.StringRelatedField(many=True)
    provider = serializers.StringRelatedField()
    commissioner = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = '__all__'
        depth = 1

