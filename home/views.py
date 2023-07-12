from django.shortcuts import render
from person.models import Persona
# Create your views here.

def index(request):
    persons = Persona.objects.all()
    context = {'persons':persons}
    return render(request, 'home/index.html', context)