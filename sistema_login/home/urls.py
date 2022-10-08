from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.inicial, name='inicial'),
    path('add_equipe', views.add_equipe, name='add_equipe'),
    path('add_estudo', views.add_estudo, name='add_estudo'), #logado
    path('add_usuario', views.add_usuario, name='add_usuario'),
    path('estudo_list', views.estudo_list, name='estudo_list'), #logado
]