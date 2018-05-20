# coding: utf-8
from rest_framework import serializers
from .models import *


class DutySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class IntellectualPropertySerializer(serializers.ModelSerializer):
    contract_type = serializers.StringRelatedField()
    provider = serializers.StringRelatedField()
    commissioner = serializers.StringRelatedField()
    ground = serializers.StringRelatedField()
    type_fk = serializers.StringRelatedField()
    owners = serializers.StringRelatedField(many=True)
    creators = serializers.StringRelatedField(many=True)
    countries = serializers.StringRelatedField(many=True)
    duty_payments = serializers.StringRelatedField(many=True)

    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        depth = 1


class IntellectualPropertyCommercializationSerializer(serializers.ModelSerializer):
    intellectual_property = serializers.StringRelatedField()
    commercialization_type = serializers.StringRelatedField()
    licenser = serializers.StringRelatedField(many=True)

    class Meta:
        model = IPCommercialization
        fields = '__all__'
        depth = 1


class IntangibleAssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = IntangibleAssets
        fields = '__all__'
        depth = 1


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = '__all__'
