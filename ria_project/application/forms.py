from django import forms
from application.models import Request


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs = {
                'class': 'form-control',
                'placeholder': field.help_text,
            }

        self.fields['priority_date'].widget.attrs['type'] = 'date'
        self.fields['is_contracted'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Request
        fields = '__all__'