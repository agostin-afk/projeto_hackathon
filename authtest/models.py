from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    numero = models.PositiveIntegerField()
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=60)
    numeracao = models.IntegerField()
    descricao = models.TextField()
    qtd_estoque = models.PositiveIntegerField()
    