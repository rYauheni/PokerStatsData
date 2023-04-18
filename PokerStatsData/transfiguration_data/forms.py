from django import forms
from .models import Data


class InputDataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('input_data',)
        labels = {
            'input_data': 'InputData',
        }
        widgets = {
            'input_data': forms.Textarea(attrs={
                'placeholder': 'Enter the data...',
                'rows': 1,
            }),
        }
