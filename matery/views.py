from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from matery.models import matery
from matery.forms import FormMatery
from django.urls import reverse_lazy


# Create your views here.

class añadirMateria(PermissionRequiredMixin,CreateView):
	model = matery
	form_class = FormMatery
	template_name = 'matery/matery.html'
	success_url = reverse_lazy('home')
	permission_required = {'usuario.permiso_admin'}