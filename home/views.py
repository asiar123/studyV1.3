from django.shortcuts import render
from person.models import Persona
# Create your views here.

def index(request):
    person = Persona.objects.all()
    context = {'patients':person}
    return render(request, 'home/index.html', context)