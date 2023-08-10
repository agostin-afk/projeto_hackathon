from django.db import models

# vamo criar as models
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    numero = models.PositiveIntegerField()

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    numeracao = models.IntegerField()
    descricao = models.TextField()
    qtd_estoque = models.PositiveIntegerField()
    