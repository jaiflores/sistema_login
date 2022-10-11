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
        fields = ('user', 'password', 'email',)

class EstudoForm(ModelForm):
    class Meta:
        model = Estudo
        fields = ('name_study','descricao', 'x', 'y',) #'usuario_user_id' quando estiver sendo gerado automaticamente