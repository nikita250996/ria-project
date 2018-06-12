from django import forms
from application.models import IntellectualProperty, Payment, IntangibleAssets, IPCommercialization


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

