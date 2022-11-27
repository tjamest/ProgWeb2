from django import forms
from contatos.models import Pessoa







class ContatoModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label = 'Data Nascimento',
        help_text = "Nascimento formato dd/mm/AAAA",
    )

    
    class Meta:
        model = Pessoa
        fields = '__all__'