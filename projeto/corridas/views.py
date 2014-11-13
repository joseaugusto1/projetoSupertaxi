from django.shortcuts import render
from corridas.forms import CorridasForm

def index(request):
    form = CorridasForm()
    return render(request, 'index.html',{'form':form})

def validar(request):
	if request.method =="POST":
        form = CorridasForm(request.POST)
        
        if form.is_valid():
            corridas = Corridas(**form.cleaned_data)
            corridas.save()
            
            corridas = Corridas.objects.all()
            
            return render(request,'validar.html',{'form':form,'corridas':corridas})
        

		
        