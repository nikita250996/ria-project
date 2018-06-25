# coding: utf-8
import os
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets
from . import serializers
from . import models
from . import forms
from application.documentation import wb_proc


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


# ------------------------------------------------------------------------------
# ПЕЧАТЬ ДОКУМЕНТОВ
# ------------------------------------------------------------------------------

# ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ - вложение
def attachment(document, name, format_as_string):
    response = HttpResponse(
        document, content_type='application/{0}'.format(format_as_string))
    response['Content-Length'] = os.path.getsize(wb_proc.FILE)
    os.remove(wb_proc.FILE)
    cntnt = 'attachment; filename={0}_{1}.docx'.format(name, wb_proc.today())
    response['Content-Disposition'] = cntnt

    return response

# СЛУЖЕБНАЯ НА ОПЛАТУ ПОШЛИН - форма
def payment_req(request):
    form = forms.RequestPayment(request.POST)
    if form.is_valid():
        doc_number = form.cleaned_data['doc_number']

    return render(request, 'reports/payment_req.html', {'form': form})

# СЛУЖЕБНАЯ НА ОПЛАТУ ПОШЛИН - печать
def print_payment_req(request):
    doc_number = request.POST['doc_number']

    document = wb_proc.payment_request_docx(doc_number)

    response = attachment(document, 'Sluzhebnaya_na_oplatu_poshlin', 'docx')
    return response

# ИНФОРМАЦИЯ О ЗАЯВКАХ - форма
def requests_statistics(request):
    form = forms.RequestsStatistics(request.POST)
    if form.is_valid():
        year = form.cleaned_data['year']
        ip_type = form.cleaned_data['ip_type']

    return render(request, 'reports/requests_statistics.html', {'form': form})


# ИНФОРМАЦИЯ О ЗАЯВКАХ - печать
def print_requests_statistics(request):
    ip_type = request.POST['ip_type']
    year = request.POST['year']

    if 'docx' in request.POST:
        document = wb_proc.requests_statistics_docx(ip_type, year)
        response = attachment(document, 'Kolichestvo_zayavok', 'docx')
    elif 'xlsx' in request.POST:
        document = wb_proc.requests_statistics_xlsx(ip_type, year)
        response = attachment(document, 'Kolichestvo_zayavok', 'xlsx')
    return response


# ИНФОРМАЦИЯ О ПАТЕНТАХ - форма
def patents_statistics(request):
    form = forms.PatentsStatistics(request.POST)
    if form.is_valid():
        year = form.cleaned_data['year']
        contract_type = form.cleaned_data['contract_type']

    return render(request, 'reports/patents_statistics.html', {'form': form})


# ИНФОРМАЦИЯ О ПАТЕНТАХ - печать
def print_patents_statistics(request):
    year = request.POST['year']
    contract_type = request.POST['contract_type']

    if 'docx' in request.POST:
        document = wb_proc.patents_statistics_docx(contract_type, year)
        response = attachment(document, 'Spisok_patentov', 'docx')
    elif 'xlsx' in request.POST:
        document = wb_proc.patents_statistics_xlsx(ip_type, year)
        response = attachment(document, 'Spisok_patentov', 'xlsx')

    return response


# СПИСОК ПАТЕНТОВ ПО ОПЛАТЕ ПОШЛИН НА ПОДДЕРЖАНИЕ - форма
def maintenance_of_patents(request):
    form = forms.MaintenanceOfPatents(request.POST)
    if form.is_valid():
        sorting_field = form.cleaned_data['sorting_field']

    return render(request, 'reports/maintenance_of_patents.html', {'form': form})


# СПИСОК ПАТЕНТОВ ПО ОПЛАТЕ ПОШЛИН НА ПОДДЕРЖАНИЕ - печать
def print_maintenance_of_patents(request):
    filename = 'Spisok_patentov_na_podderzhanie'
    sorting_field = request.POST['sorting_field']

    if 'docx' in request.POST:
        document = wb_proc.maintenance_of_patents_docx(sorting_field)
        response = attachment(document, filename, 'docx')
    elif 'xlsx' in request.POST:
        document = wb_proc.maintenance_of_patents_xlsx(sorting_field)
        response = attachment(document, filename, 'xlsx')

    return response


# СПИСОК ДЕЙСТВУЮЩИХ ПАТЕНТОВ - форма
def actual_patents(request):
    form = forms.ActualPatents(request.POST)
    if form.is_valid():
        doc_number = form.cleaned_data['doc_number']
        duty = form.cleaned_data['duty']

    return render(request, 'reports/actual_patents.html', {'form': form})


# СПИСОК ДЕЙСТВУЮЩИХ ПАТЕНТОВ - печать
def print_actual_patents(request):
    ip_type = request.POST['ip_type']

    document = wb_proc.actual_patents(ip_type)

    if 'docx' in request.POST:
        document = wb_proc.patents_statistics_docx(contract_type, year)
        response = attachment(document, 'Spisok_deystvuyuschih_patentov', 'docx')
    elif 'xlsx' in request.POST:
        document = wb_proc.patents_statistics_xlsx(ip_type, year)
        response = attachment(document, 'Spisok_deystvuyuschih_patentov', 'xlsx')

    return response


# ИНФОРМАЦИЯ ОБ ОПЛАЧЕННЫХ ПОШЛИНАХ - форма
def payments(request):
    form = forms.Payments(request.POST)
    if form.is_valid():
        year = form.cleaned_data['year']
        is_supported = form.cleaned_data['is_supported']

    return render(request, 'reports/payments.html', {'form': form})


# НФОРМАЦИЯ ОБ ОПЛАЧЕННЫХ ПОШЛИНАХ - печать
def print_payments(request):
    year = request.POST['year']
    is_supported = request.POST.get('is_supported', False)

    if 'docx' in request.POST:
        document = wb_proc.payments_docx(year, is_supported)
        response = attachment(document, 'Oplachennye_poshliny', 'docx')

    return response


# СПИСОК ДЕЙСТВУЮЩИХ ПАТЕНТОВ - форма
def table23(request):
    form = forms.Table23(request.POST)
    if form.is_valid():
        year = form.cleaned_data['year']

    return render(request, 'reports/table23.html', {'form': form})


# СПИСОК ДЕЙСТВУЮЩИХ ПАТЕНТОВ - печать
def print_table23(request):
    year = request.POST['year']

    if 'docx' in request.POST:
        document = wb_proc.table_23_docx(year)
        response = attachment(document, 'Table_23', 'docx')

    return response

  
class MessageCreate(CreateView):
    model = models.Message
    form_class = forms.MessageForm
    success_url = reverse_lazy('sent_messages')
    template_name = 'application/write_message_form.html'

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
        message = models.Message.objects.get(id=self.kwargs['pk'])
        form = self.form_class(message=message)
        return render(request, self.template_name, {'form': form, 'message': message})


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

    def form_valid(self, form):
        clean = form.cleaned_data
        context = {}
        self.object = context.save(clean)
        return super(MessageOpen, self).form_valid(form)
