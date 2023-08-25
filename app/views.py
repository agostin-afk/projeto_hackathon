from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import Usuario

def lista(request):
    pessoas = User.objects.all()
    return render(request, 'lista.html', {"pessoas": pessoas})

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username = username).first()
        if user: 
            return HttpResponse('já existe um usuário com esse nome, tente novamente')
        
        user = User.objects.create_user(username, email, senha)
        
        return HttpResponse(username)
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else: 
        username = request.POST.get("username")
        senha = request.POST.get("senha")
        user = authenticate(username=username,password=senha)
        
        if user: 

            login_django(request, user)

            return render(request, "produtos.html")
        else: 
            return HttpResponse("Email ou senha inválidos")
'''      
sem o login_required:
def produtos(request):
    if request.user.is_authenticated:
        return HttpResponse('pagina dos produtos')
    else: 
        return HttpResponse("você precisa estar logado!!!")
'''
@login_required(login_url="/auth/login/")
def produtos(request):
    if request.method == "GET":
        return render(request, 'produtos.html')