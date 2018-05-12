from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from . import serializers
from . import models


class RequestViewSet(viewsets.ModelViewSet):
    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer


class RequestCreate(CreateView):
    model = models.Request
    fields = '__all__'


class RequestUpdate(UpdateView):
    model = models.Request
    fields = '__all__'
    success_url = reverse_lazy('index')


class DutyPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.DutySerializer


class IntellectualPropertyViewSet(viewsets.ModelViewSet):
    queryset = models.IntellectualProperty.objects.all()
    serializer_class = serializers.IntellectualPropertySerializer


class ContractIntellectualPropertyViewSet(viewsets.ModelViewSet):
    queryset = models.ContractIntellectualProperties.objects.all()
    serializer_class = serializers.ContractIntellectualPropertySerializer


class IntellectualPropertyCommercializationViewSet(viewsets.ModelViewSet):
    queryset = models.IPCommercialization.objects.all()
    serializer_class = serializers.IntellectualPropertyCommercializationSerializer


class IntangibleAssetViewSet(viewsets.ModelViewSet):
    queryset = models.IntangibleAssets.objects.all()
    serializer_class = serializers.IntangibleAssetSerializer