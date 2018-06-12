# coding: utf-8
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets
from . import serializers
from . import models
from . import forms


# VIEW SETS FOR REST API
# оплаты пошлин
class DutyPaymentViewSet(viewsets.ModelViewSet):
    queryset = models.Payment.objects.all()
    serializer_class = serializers.DutySerializer


# РИД
class IntellectualPropertyViewSet(viewsets.ModelViewSet):
    queryset = models.IntellectualProperty.objects.all()
    serializer_class = serializers.IntellectualPropertySerializer

    def get_queryset(self):
        user = self.request.user
        queryset = models.IntellectualProperty.objects.all()

        if user.is_authenticated and not user.is_superuser:
            queryset = queryset.filter(ground__ground_code=user.employeeinfo.ground.ground_code)

        is_request_param = self.request.query_params.get('request', None)
        if is_request_param:
            queryset = queryset.filter(is_request=is_request_param)

        is_contracted_param = self.request.query_params.get('contracted', None)
        if is_contracted_param:
            queryset = queryset.filter(is_contracted=is_contracted_param)

        return queryset


# коммерциализация РИД
class IntellectualPropertyCommercializationViewSet(viewsets.ModelViewSet):
    queryset = models.IPCommercialization.objects.all()
    serializer_class = serializers.IntellectualPropertyCommercializationSerializer


# реестр НМА
class IntangibleAssetViewSet(viewsets.ModelViewSet):
    queryset = models.IntangibleAssets.objects.all()
    serializer_class = serializers.IntangibleAssetSerializer


# уведомления
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerializer

    def get_queryset(self):
        queryset = models.Notification.objects.all()

        read_param = self.request.query_params.get('read', None)
        if read_param:
            queryset = queryset.filter(read=read_param)

        return queryset


# ФОРМЫ
# добавить заявку
class RequestCreate(SuccessMessageMixin, CreateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    success_message = 'Заявка была добавлена.'
    template_name = 'application/request_form.html'


# редактировать заявку
class RequestUpdate(SuccessMessageMixin, UpdateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    success_message = 'Заявка была изменена.'
    template_name = 'application/request_form.html'


# редактировать РИД
class IPUpdate(SuccessMessageMixin, UpdateView):
    model = models.IntellectualProperty
    form_class = forms.IntellectualPropertyForm
    success_url = reverse_lazy('intellectual_properties')
    success_message = "РИД c названием '{name}' был изменен."
    template_name = 'application/intellectual_property_form.html'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(name=self.object.name)

    def get(self, request, *args, **kwargs):
        instance = models.IntellectualProperty.objects.get(id=kwargs['pk'])
        payments = instance.duty_payments.all()
        form = self.form_class(instance=instance)
        return render(request, self.template_name, {'form': form, 'payments': payments})


# редактировать РИД по договору
class IPContractUpdate(SuccessMessageMixin, UpdateView):
    model = models.IntellectualProperty
    form_class = forms.ContractIntellectualPropertyForm
    success_url = reverse_lazy('contract_intellectual_properties')
    success_message = "РИД c названием '{name}' был изменен."
    template_name = 'application/contract_intellectual_property_form.html'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(name=self.object.name)


# добавить запись реестра НМА
class IntAssetCreate(SuccessMessageMixin, CreateView):
    model = models.IntangibleAssets
    form_class = forms.IntangibleAssetForm
    success_url = reverse_lazy('intangible_assets')
    success_message = "В реестр НМА добавлена новая запись."
    template_name = 'application/intangible_assets_form.html'


# редактировать запись реестра НМА
class IntAssetUpdate(SuccessMessageMixin, UpdateView):
    model = models.IntangibleAssets
    form_class = forms.IntangibleAssetForm
    success_url = reverse_lazy('intangible_assets')
    success_message = "Запись в реестре обновлена."
    template_name = 'application/intangible_assets_form.html'


# добавить оплату пошлины
class PaymentCreate(SuccessMessageMixin, CreateView):
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payments')
    success_message = "Добавлена новая запись."
    template_name = 'application/payment_form.html'


# редактировать оплату пошлины
class PaymentUpdate(SuccessMessageMixin, UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payments')
    success_message = "Запись обновлена."
    template_name = 'application/payment_form.html'


# добавить коммерциализацию РИд
class IPCommercializationCreate(SuccessMessageMixin, CreateView):
    model = models.IPCommercialization
    form_class = forms.IPCommercializationForm
    success_url = reverse_lazy('intellectual_properties_commercialization')
    success_message = "Добавлена новая запись."
    template_name = 'application/ip_commercialization_form.html'


# редактировать коммерциализацию РИД
class IPCommercializationUpdate(SuccessMessageMixin, UpdateView):
    model = models.IPCommercialization
    form_class = forms.IPCommercializationForm
    success_url = reverse_lazy('intellectual_properties_commercialization')
    success_message = "Запись обновлена."
    template_name = 'application/ip_commercialization_form.html'
