from datetime import timedelta
from django import forms
from django.utils.timezone import now
from main.models import Emprestimo

class ReservaForm(forms.ModelForm):
    data_devolucao = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'block w-full mt-1 border-gray-300 rounded-md shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
        }),
        label="Data Devolução Prevista",
        initial=(now() + timedelta(days=14)).date()
    )

    class Meta:
        model = Emprestimo
        fields = ['data_devolucao']