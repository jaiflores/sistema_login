from django.forms import ModelForm
from .models import Equipe,Usuario, Estudo


# Create a Equipe form

class EquipeForm(ModelForm):
    class Meta:
        model = Equipe
        fields = ('team_id','team_desc',)

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario 
        fields = ('user', 'password', 'email', 'equipe_team',)

class EstudoForm(ModelForm):
    class Meta:
        model = Estudo
        fields = ('descricao', 'x', 'y',)