# coding: utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets

from application.models import Message
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


# сообщения
class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer

    def get_queryset(self):
        queryset = models.Message.objects.all()
        #http://127.0.0.1:8000/сообщения/входящие
        if self.request.META['HTTP_REFERER'] == 'http://' + self.request.get_host() + '/%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F/%D0%B2%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B8%D0%B5':
            queryset = queryset.filter(receiver=self.request.user.id)
        #http://127.0.0.1:8000/сообщения/исходящие
        if self.request.META['HTTP_REFERER'] == 'http://' + self.request.get_host() + '/%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D1%8F/%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D1%8F%D1%89%D0%B8%D0%B5':
            queryset = queryset.filter(sender=self.request.user.id)
        return queryset


# FORMS
# добавить заявку
class RequestCreate(CreateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    template_name = 'application/request_form.html'


# редактировать заявку
class RequestUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.RequestIntellectualPropertyForm
    success_url = reverse_lazy('index')
    template_name = 'application/request_form.html'


# редактировать РИД
class IPUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.IntellectualPropertyForm
    success_url = reverse_lazy('intellectual_properties')
    template_name = 'application/intellectual_property_form.html'


# редактировать РИД по договору
class IPContractUpdate(UpdateView):
    model = models.IntellectualProperty
    form_class = forms.ContractIntellectualPropertyForm
    success_url = reverse_lazy('contract_intellectual_properties')
    template_name = 'application/contract_intellectual_property_form.html'


# добавить запись реестра НМА
class IntAssetCreate(CreateView):
    model = models.IntangibleAssets
    form_class = forms.IntangibleAssetForm
    success_url = reverse_lazy('intangible_assets')
    template_name = 'application/intangible_assets_form.html'


# редактировать запись реестра НМА
class IntAssetUpdate(UpdateView):
    model = models.IntangibleAssets
    form_class = forms.IntangibleAssetForm
    success_url = reverse_lazy('intangible_assets')
    template_name = 'application/intangible_assets_form.html'


# добавить оплату пошлины
class PaymentCreate(CreateView):
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payments')
    template_name = 'application/payment_form.html'


# редактировать оплату пошлины
class PaymentUpdate(UpdateView):
    model = models.Payment
    form_class = forms.PaymentForm
    success_url = reverse_lazy('payments')
    template_name = 'application/payment_form.html'


# добавить коммерциализацию РИд
class IPCommercializationCreate(CreateView):
    model = models.IPCommercialization
    form_class = forms.IPCommercializationForm
    success_url = reverse_lazy('intellectual_properties_commercialization')
    template_name = 'application/ip_commercialization_form.html'


# редактировать коммерциализацию РИД
class IPCommercializationUpdate(UpdateView):
    model = models.IPCommercialization
    form_class = forms.IPCommercializationForm
    success_url = reverse_lazy('intellectual_properties_commercialization')
    template_name = 'application/ip_commercialization_form.html'


class MessageCreate(CreateView):
    model = models.Message
    form_class = forms.MessageForm
    success_url = reverse_lazy('sent_messages')
    template_name = 'application/write_message_form.html'

    #def post(self, request, *args, **kwargs):
    #    my_some = "HARDHAT"
    #    return TemplateResponse(request, self.template_name, {"my_some": my_some})

    def get_form_kwargs(self):
        kwargs = super(MessageCreate, self).get_form_kwargs()
        kwargs.update({
            'request': self.request
        })
        return kwargs


class MessageRead(CreateView):
    model = models.Message
    form_class = forms.MessageAnswerForm
    success_url = reverse_lazy('received_messages')
    template_name = 'application/answer_message_form.html'

    def get(self, request, *args, **kwargs):
        message = Message.objects.get(id=self.kwargs['pk'])
        form = self.form_class(message=message)
        return render(request, self.template_name, {'form': form, 'message': message})

    # def get_form_kwargs(self):
    #     kwargs = super(MessageRead, self).get_form_kwargs()
    #     kwargs.update({
    #         'message': self.message,
    #     })
    #     return kwargs


class MessageOpen(UpdateView):
    model = models.Message
    form_class = forms.MessageForm
    success_url = reverse_lazy('sent_messages')
    template_name = 'application/open_message_form.html'

    def get_form_kwargs(self):
        kwargs = super(MessageOpen, self).get_form_kwargs()
        kwargs.update({
            'request': self.request
        })
        return kwargs

    #def get_read(self, queryset=None):
    #   return self.request.read

    def form_valid(self, form):
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(MessageOpen, self).form_valid(form)