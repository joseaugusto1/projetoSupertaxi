from django.shortcuts import render
from corridas.forms import CorridasForm

def index(request):
    form = CorridasForm()
    return render(request, 'index.html',{'form':form})

