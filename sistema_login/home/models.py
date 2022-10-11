from django.db import models
from django.contrib.auth.models import User

class Equipe(models.Model):
    team_id = models.CharField(max_length=150, primary_key=True)
    team_desc = models.TextField(blank=True)
    # team_data_criacao = models.DateTimeField('Criação', auto_now_add=True)

    def __str__(self):
        return self.team_id

class Usuario(models.Model):
    user_id = models.CharField(max_length=50, primary_key=True)
    user = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField('User Email' )
    # user_data_criacao = models.DateTimeField('Data de Criação', auto_now_add=True)
    permissoes = models.CharField(max_length=150)
    equipe_team = models.ForeignKey(Equipe, on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={'team_id': True}) 

    def __str__(self):
        return f'{self.user}, {self.email}'

class Estudo(models.Model):
    # study_id = models.CharField(max_length=50, primary_key=True)
    name_study = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    x = models.CharField(max_length=50)
    y = models.CharField(max_length=50)
    # data_entrada = models.DateTimeField('Data de entrada', auto_now_add=True)
    usuario_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={'user_id': True})
    # team_study = models.BooleanField(default=True, blank = True)

    def __str__(self):
        return self.name_study
    def __str__(self):
        return self.descricao
    def __repr__(self):
        return f'x={self.x}\ny={self.y}'

# equipe = {
#     'team_id': int,
#     'team_desc': str,
#     'team_data_criacao': dt,
# }

# usuario = {
#     'user_id': str,
#     'user': str,
#     'pwd': any,
#     'email': str,
#     'user_data_criacao': dt,
#     'permissoes': list,
#     'equipe_team_id': list,
# }

# estudos = {
#     'study_id': int,
#     'descrição': str,
#     'x': list,
#     'y': list,
#     'data_entrada': dt,
#     'usuario.user_id': int,
#     'team_study': bool, #False
# }