from django import forms
from application.models import Request, Payment


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        self.fields['priority_date'].widget.attrs['type'] = 'date'

    class Meta:
        model = Request
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
