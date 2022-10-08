from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EquipeForm, UsuarioForm, EstudoForm 
from .models import Estudo


def inicial(request):
    return render(request, 'home/home.html')

def home(request):
    return render(request, 'home/home.html')

def estudo_list(request):
    estudo_list = Estudo.objects.all()
    return render(request, 'home/estudo_list.html', 
    {'estudo_list': estudo_list})

def add_equipe(request):
    submitted = False
    if request.method == "POST":
        form = EquipeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_equipe?submitted=True')
    else: 
        form = EquipeForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/add_equipe.html',{'form':form, 'submitted': submitted })

def add_usuario(request):
    submitted = False
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_usuario?submitted=True')
    else:
        form = UsuarioForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/add_usuario.html',{'form':form, 'submitted': submitted })

def add_estudo(request):
    form = EstudoForm

    # submitted = False
    # if request.method == "POST":
    #     form = EstudoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/add_estudo?submitted=True')
    # else:
    #     form = EstudoForm
    #     if 'submitted' in request.GET:
    #         submitted = True

    return render(request, 'home/add_estudo.html',{'form':form})
