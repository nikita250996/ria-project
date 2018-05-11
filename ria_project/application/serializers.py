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


class DutySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class IntellectualPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        depth = 1


class ContractIntellectualPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = ContractIntellectualProperties
        fields = '__all__'
        depth = 1


class IntellectualPropertyCommercializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = IPCommercialization
        fields = '__all__'
        depth = 1


class IntangibleAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntangibleAssets
        fields = '__all__'
        depth = 1