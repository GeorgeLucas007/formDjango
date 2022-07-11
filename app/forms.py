from django.forms import ModelForm
from app.models import dadosPessoal
from django import forms

class dadosPessoalForm(ModelForm):
    class Meta:
        model = dadosPessoal
        fields = ['primeiroNome', 'ultimoNome']


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982', '1983', '1984', '1985']

FAVORITE_COLORS_CHOICES = [
    ('fundamental', 'Fundamental'),
    ('médio', 'Médio'),
    ('superior', 'Superior')
]

class SimpleForm(forms.Form):

    Nasceu = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    Nível = forms.ChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )