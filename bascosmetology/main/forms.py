from django.forms import ModelForm, TextInput, EmailInput, Select, DateInput, TimeInput, CheckboxInput
from .models import Records, Category


class RecordsForm(ModelForm):

    class Meta:
        model = Records
        fields = ['name', 'email', 'procedure', 'date', 'time', 'newsletter']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Имя"

            }),
            'email': EmailInput(attrs={
                'placeholder': "el.pochta@primer.ru"

            }),
            'procedure': Select(attrs={


            }),
            'date': DateInput(attrs={
                'type': 'date'

            }),
            'time': TimeInput(attrs={
                'type': 'time'
            }),
            'newsletter': CheckboxInput(attrs={
                'class': 'news',
            }),
        }
