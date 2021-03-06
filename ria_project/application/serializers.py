# coding: utf-8
from rest_framework import serializers
from .models import *


class DutySerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class IntellectualPropertySerializer(serializers.ModelSerializer):
    duty_payments = serializers.StringRelatedField(many=True)
    countries = serializers.StringRelatedField(many=True)
    owners = serializers.StringRelatedField(many=True)
    creators = serializers.StringRelatedField(many=True)
    provider = serializers.StringRelatedField()
    commissioner = serializers.StringRelatedField()
    contract_type = serializers.StringRelatedField()
    type_fk = serializers.StringRelatedField()
    ground = serializers.StringRelatedField()
    class_fication = serializers.StringRelatedField()

    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        depth = 1


class IntellectualPropertyCommercializationSerializer(serializers.ModelSerializer):
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


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = '__all__'
        depth = 1
