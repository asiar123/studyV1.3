from django.views.generic import CreateView
from biology.models import Biology
from biology.forms import FormBiology
from django.urls import reverse_lazy

# Create your views here.

class añadirBiology(CreateView):
	model = Biology
	form_class = FormBiology
	template_name = 'biology/new-biology.html'
	success_url = reverse_lazy('english')