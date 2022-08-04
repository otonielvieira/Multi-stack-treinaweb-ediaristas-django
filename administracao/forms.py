from decimal import Decimal
from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}));
    class Meta:
        model = Servico
        fields = '__all__'
        
    def clean_valor_minimo(self):
        data = self.cleaned_data['valor_minimo']
        return Decimal(data.replace(',', '.'))


         