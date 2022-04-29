from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants


# Create your views here.


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/coletanea/minha_coletanea')

    if request.method == "GET":
        return render(request, 'cadastro.html')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Dados inválidos! Tente novamente.')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Este usuário já existe! Tente novamente.')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, email=email, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
            return redirect('/auth/logar')
        except:
            messages.add_message(request, constants.ERROR, 'Erro inesperado, tente novamente.')
            return redirect('/auth/cadastro')




def logar(request):
    if request.user.is_authenticated:
        return redirect('/coletanea/minha_coletanea')
        
    if request.method == 'GET':
        return render(request, 'logar.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
            return redirect('/auth/logar')
        else:
            auth.login(request, user)
            return redirect('/coletanea/minha_coletanea')



def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')