from django import forms
from django.forms import ModelForm
from .models import Equipe,Estudo

# Create a Equipe form

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ('team_id','team_desc',)

class EstudoForm(ModelForm):
    class Meta:
        model = Estudo
        fields = ('name_study','descricao', 'x', 'y','usuario_user_id') #'usuario_user_id' quando estiver sendo gerado automaticamente
        labels = {
            'name_study': 'Nome do Estudo',
            'descricao': 'Descrição do Estudo',
            'x': 'Valor de x',
            'y': 'Valor de y',
        }
        widgets = {
            'name_study': forms.TextInput(attrs={'class':'camplog', 'placeholder':'Nome do Estudo'}),
            'descricao': forms.TextInput(attrs={'class':'camplog', 'placeholder':'Descrição do Estudo'}),
            'x': forms.TextInput(attrs={'class':'camplog', 'placeholder':'Valor de x'}),
            'y':  forms.TextInput(attrs={'class':'camplog', 'placeholder':'Valor de y'}),
        }
