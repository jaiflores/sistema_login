from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/estudo_list')
		else:
			messages.success(request, ("Username ou senha não conferem. Verifique e tente novamente!"))	
			return redirect('login')	
	else:
		return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, (" Você não esta logado! "))	
    return redirect('/home')

def register_user(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request,user)
			messages.success(request, ("Registro concluido!"))
			return redirect('/home')
	else:
		form = RegisterUserForm()

	return render (request, 'authenticate/register_user.html', {'form': form})
	
