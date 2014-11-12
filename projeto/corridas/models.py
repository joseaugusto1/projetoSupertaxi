from django.db import models

class Corridas(models.Model):
    nome = models.CharField(max_length=100)
    enderecoBusca = models.CharField(max_length=200)
    enderecoLeva = models.CharField(max_length=200)
    tel = models.CharField(max_length=15) 
    andamento = models.BooleanField(default=True)
    
    
    