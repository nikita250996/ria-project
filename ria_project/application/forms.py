from django import forms
from application.models import IntellectualProperty, Payment, IntangibleAssets, IPCommercialization, Message, User
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
    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        exclude = ('duty_payments', 'is_request', 'send_date')
        widgets = {
            'priority_date': forms.DateInput(attrs={'type': 'date'}),
            'receipt_date': forms.DateInput(attrs={'type': 'date'}),
            'grant_date': forms.DateInput(attrs={'type': 'date'}),
            'contract_date': forms.DateInput(attrs={'type': 'date'}),
            'bulletin_date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.Textarea(attrs={'rows': '4'}),
            'abridgement': forms.Textarea(attrs={'rows': '4'}),
            'note': forms.Textarea(attrs={'rows': '3'}),
        }


class ContractIntellectualPropertyForm(forms.ModelForm):
    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        exclude = ('duty_payments', 'is_supported', 'is_request', 'send_date', 'is_contracted')
        widgets = {
            'priority_date': forms.DateInput(attrs={'type': 'date'}),
            'receipt_date': forms.DateInput(attrs={'type': 'date'}),
            'grant_date': forms.DateInput(attrs={'type': 'date'}),
            'contract_date': forms.DateInput(attrs={'type': 'date'}),
            'bulletin_date': forms.DateInput(attrs={'type': 'date'}),
            'text': forms.Textarea(attrs={'rows': '4'}),
            'abridgement': forms.Textarea(attrs={'rows': '4'}),
            'note': forms.Textarea(attrs={'rows': '3'}),
        }


class PaymentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        self.fields['intellectual_property'].queryset = IntellectualProperty.objects.filter(is_request=False)
        # self.fields['intellectual_property'].queryset = IntellectualProperty.objects.all

    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'payment_date': forms.DateInput(attrs={'type': 'date'}),
            'posted_date': forms.DateInput(attrs={'type': 'date'}),
            'note': forms.Textarea(attrs={'rows': '4'}),
        }


class IntangibleAssetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IntangibleAssetForm, self).__init__(*args, **kwargs)

        self.fields['intellectual_property'].queryset = IntellectualProperty.objects.filter(is_request=False)

    class Meta:
        model = IntangibleAssets
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'retirement_date': forms.DateInput(attrs={'type': 'date'}),
        }


class IPCommercializationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IPCommercializationForm, self).__init__(*args, **kwargs)

        self.fields['intellectual_property'].queryset = IntellectualProperty.objects.filter(is_request=False)

    class Meta:
        model = IPCommercialization
        fields = '__all__'
        widgets = {
            'filing_date': forms.DateInput(attrs={'type': 'date'}),
            'contract_duration': forms.DateInput(attrs={'type': 'date'}),
            'send_date': forms.DateInput(attrs={'type': 'date'}),
        }


class MessageAnswerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.message = kwargs.pop('message', None)
        super(MessageAnswerForm, self).__init__(*args, **kwargs)

        if self.message:
            self.fields['sender'].initial = User.objects.get(id=self.message.receiver.id)
            self.fields['receiver'].initial = User.objects.get(id=self.message.sender.id)

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

        self.fields['sender'].initial = User.objects.get(id=get_user(self.request).id)
        self.fields['receiver'].queryset = User.objects.filter(~Q(id=get_user(self.request).id))

    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'text': forms.Textarea(attrs={'rows': '6'}),
            'sender': forms.HiddenInput(),
            'read': forms.HiddenInput(),
        }
