from django import forms
from application.models import IntellectualProperty, Payment, IntangibleAssets, IPCommercialization


class RequestIntellectualPropertyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestIntellectualPropertyForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        # self.fields['priority_date'].widget.attrs['type'] = 'date'
        # self.fields['is_contracted'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = IntellectualProperty
        fields = '__all__'
        exclude = ('duty_payments',)


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
