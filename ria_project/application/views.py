from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from . import serializers
from . import models
from . import forms


# VIEW SETS FOR REST API
# class RequestViewSet(viewsets.ModelViewSet):
#     queryset = models.Request.objects.all()
#     serializer_class = serializers.RequestSerializer
#
#     def get_queryset(self):
#         user = self.request.user
#         queryset = models.Request.objects.all()
#
#         if not user.is_superuser:
#             queryset = queryset.filter(ground__ground_code=user.employeeinfo.ground.ground_code)
#
#         return queryset


class DutyPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.DutySerializer


class IntellectualPropertyViewSet(viewsets.ModelViewSet):
    queryset = models.IntellectualProperty.objects.all()
    serializer_class = serializers.IntellectualPropertySerializer


# class ContractIntellectualPropertyViewSet(viewsets.ModelViewSet):
#     queryset = models.ContractIntellectualProperties.objects.all()
#     serializer_class = serializers.ContractIntellectualPropertySerializer


class IntellectualPropertyCommercializationViewSet(viewsets.ModelViewSet):
    queryset = models.IPCommercialization.objects.all()
    serializer_class = serializers.IntellectualPropertyCommercializationSerializer


class IntangibleAssetViewSet(viewsets.ModelViewSet):
    queryset = models.IntangibleAssets.objects.all()
    serializer_class = serializers.IntangibleAssetSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer

    def get_queryset(self):
        queryset = models.Notification.objects.all()

        read_param = self.request.query_params.get('read', None)
        if read_param:
            queryset = queryset.filter(read=read_param)

        return queryset


# FORMS
class RequestCreate(CreateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    template_name = 'application/request_form.html'


class RequestUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    template_name = 'application/request_form.html'


class IPUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.IntellectualPropertyForm
    success_url = reverse_lazy('intellectual_properties')
    template_name = 'application/intellectual_property_form.html'


class IPContractUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.ContractIntellectualPropertyForm
    success_url = reverse_lazy('contract_intellectual_properties')
    template_name = 'application/contract_intellectual_property_form.html'


class IntAssetCreate(CreateView):
    model = models.IntangibleAssets
    fields = '__all__'
    success_url = reverse_lazy('intangible_assets')


class IntAssetUpdate(UpdateView):
    model = models.IntangibleAssets
    fields = '__all__'
    success_url = reverse_lazy('intangible_assets')


class PaymentCreate(CreateView):
    model = models.Payment
    fields = '__all__'
    success_url = reverse_lazy('payments')


class PaymentUpdate(UpdateView):
    model = models.Payment
    fields = '__all__'
    success_url = reverse_lazy('payments')


class IPCommercializationCreate(CreateView):
    model = models.IPCommercialization
    fields = '__all__'
    success_url = reverse_lazy('intellectual_properties_commercialization')


class IPCommercializationUpdate(UpdateView):
    model = models.IPCommercialization
    fields = '__all__'
    success_url = reverse_lazy('intellectual_properties_commercialization')
