from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'gerador/index.html',{
        'number':number()
    })
def number():
    numbers = [random.randrange(1,60,1)for i in range (6)]
    #list comprehension
    #gerando numeros aleatórios de 1 a 60 (1 é o intervalo)
    return numbers