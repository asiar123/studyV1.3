from django.shortcuts import render, redirect
from person.forms import formularioPersona

# Create your views here.

def newPerson(request):
    if request.method == 'POST':
        form = formularioPersona(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = formularioPersona()
    return render(request, 'person/new-person.html', {'form':form})