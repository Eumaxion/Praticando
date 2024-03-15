from django.db import models

# Create your models here.
class Horas(models.Model):
    entrada_inicial = models.DateTimeField()
    saida_inicial = models.DateTimeField()
    entrada_final = models.DateTimeField()
    saida_final = models.DateTimeField()
