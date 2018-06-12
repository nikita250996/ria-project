from django import forms

from application.models import IntellectualProperty, Payment, IntangibleAssets, IPCommercialization, Message, Person, \
    PrivatePerson, EmployeeInfo
from django.db.models import Q
from django.contrib.auth import get_user


class RequestIntellectualPropertyForm(forms.ModelForm):

    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        exclude = ('duty_payments', 'is_supported', 'is_request')
        widgets = {
            'priority_date': forms.DateInput(attrs={'type': 'date'}),
            'send_date': forms.DateInput(attrs={'type': 'date'}),
            'receipt_date': forms.DateInput(attrs={'type': 'date'}),
            'grant_date': forms.DateInput(attrs={'type': 'date'}),
            'contract_date': forms.DateInput(attrs={'type': 'date'}),
            'bulletin_date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.Textarea(attrs={'rows': '4'}),
            'abridgement': forms.Textarea(attrs={'rows': '4'}),
            'note': forms.Textarea(attrs={'rows': '3'}),
        }


class IntellectualPropertyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IntellectualPropertyForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        self.fields['priority_date'].widget.attrs['type'] = 'date'
        self.fields['is_contracted'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = IntellectualProperty
        fields = '__all__'


class ContractIntellectualPropertyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ContractIntellectualPropertyForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        self.fields['priority_date'].widget.attrs['type'] = 'date'
        self.fields['is_contracted'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = IntellectualProperty
        fields = '__all__'


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        self.fields['payment_date'].widget.attrs['type']='date'
        self.fields['posted_date'].widget.attrs['type'] = 'date'

    class Meta:
        model = Payment
        fields = '__all__'


class IntangibleAssetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IntangibleAssetForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

    class Meta:
        model = IntangibleAssets
        fields = '__all__'


class IPCommercializationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IPCommercializationForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

    class Meta:
        model = IPCommercialization
        fields = '__all__'


class MessageAnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop('message', None)
        super(MessageAnswerForm, self).__init__(*args, **kwargs)

        if self.message:
            self.fields['sender'].initial = Person.objects.get(id=self.message.receiver.id)
            self.fields['receiver'].initial = Person.objects.get(id=self.message.sender.id)


    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows': '6'}),
            'sender': forms.HiddenInput(),
            'read': forms.HiddenInput(),
            'receiver': forms.HiddenInput(),
        }


class MessageForm(forms.ModelForm):

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(MessageForm, self).__init__(*args, **kwargs)

        #self.fields['sender'].initial = Person.objects.get(id=get_user(self.request).id)
        # self.fields['receiver'].queryset = PrivatePerson.objects.filter(~Q(id=get_user(self.request).id))
        self.fields['sender'].initial = PrivatePerson.objects.get(id=get_user(self.request).id)
        self.fields['receiver'].queryset = PrivatePerson.objects.filter(~Q(id=get_user(self.request).id))

    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows': '6'}),
            'sender': forms.HiddenInput(),
            'read': forms.HiddenInput(),
        }

    #def clean_read(self):
        #read = self.cleaned_data['read']
        #read = True
        #return read

    #def clean_sender(self):
        #sender = get_user(self.request)
    #    sender = Person.objects.get(id=get_user(self.request).id)
    #    return sender