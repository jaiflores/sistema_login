from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import EquipeForm, EstudoForm 
from .models import Estudo


def inicial(request):
    return render(request, 'home/home.html')

def home(request):
    return render(request, 'home/home.html')

def estudo_list(request):
    estudo_list = Estudo.objects.all()
    return render(request, 'home/estudo_list.html', 
    {'estudo_list': estudo_list})

def show_estudo(request, name_study_id):
    estudo_list = Estudo.objects.filter(pk=name_study_id)
    return render(request, 'home/show_estudo.html',{'estudo_list': estudo_list})

def update_estudo(request, estudo_id):
    estudo = Estudo.objects.get(pk=estudo_id)
    form = EstudoForm(request.POST or None, instance=estudo)
    if form.is_valid():
        form.save()
        return redirect('/estudo_list')
    
    return render(request,'home/update_estudo.html', {'estudo': estudo, 'form':form})

def search_estudo(request):
    if request.method == "POST":
        searched = request.POST['searched']
        estudos = Estudo.objects.filter(name_study__contains= searched)

        return render(request, 'home/search_estudo.html',{'searched':searched, 'estudos': estudos})
    else:
            return render(request, 'home/search_estudo.html',{})

def delete_estudo(request,name_study_id):
    estudo_list = Estudo.objects.get(pk=name_study_id)
    estudo_list.delete()
    return redirect('/estudo_list')

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

def add_estudo(request):
    submitted = False
    if request.method == "POST":
        form = EstudoForm(request.POST)
        if form.is_valid():
            form.save()
            est_name = form.cleaned_data['name_study']
            est_desc = form.cleaned_data['descricao']
            est_x = form.cleaned_data['x']
            est_y = form.cleaned_data['y']
            est_user  = form.cleaned_data['usuario_user_id']
            Estudo(est_name,est_desc,est_x,est_y, est_user)
            return redirect('/add_estudo?submitted=True')
    else:
        form = EstudoForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home/add_estudo.html', {'form': form ,'submitted': submitted})


# def add_estudo(request):
#     submitted = False
#     if request.method == "POST":
#         form = EstudoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_estudo?submitted=True')
#     else:
#         form = EstudoForm
#         if 'submitted' in request.GET:
#             submitted = True

#     return render(request, 'home/add_estudo.html',{'form':form, 'submitted': submitted})
