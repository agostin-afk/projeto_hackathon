from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def pagina_inicial(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')

def cadastroprod(request):
    if request.method == "GET":
        return render(request, 'cadastroprod.html')
    else:
        id_produto = request.POST.get('id_produto')
        nome_produto = request.POST.get('nome_produto')
        descricao = request.POST.get('descricao')
        
        produto = User.objects.filter(username= id_produto).first()
        if produto:
            return HttpResponse('produto com ID já cadastrado, tente novamente') 
        else:
            produto = User.objects.create_produto(username = nome_produto, id= id_produto, descricao= descricao)

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
