from django.urls import path
from . import views

app_name='home'
urlpatterns = [
    path('', views.home,name='home'),
    path('add_equipe', views.add_equipe, name='add_equipe'),
    path('home', views.inicial, name='inicial'), #logado
    path('add_estudo', views.add_estudo, name='add_estudo'), #logado
    path('estudo_list', views.estudo_list, name='estudo_list'), #logado
    path('show_estudo/<name_study_id>', views.show_estudo, name='show_estudo'), #logado
    path('update_estudo/<estudo_id>', views.update_estudo, name='update_estudo'), #logado
    path('search_estudo', views.search_estudo, name='search_estudo'), #logado
    path('delete_estudo/<name_study_id>', views.delete_estudo, name='delete_estudo'), #logado
]
