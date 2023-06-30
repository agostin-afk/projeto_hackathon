from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

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
        return HttpResponse(username)


def login(request):
    return render(request, 'login.html')