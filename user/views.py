from django.views.generic.edit import FormView
from user.forms import FormularioLogin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from user.forms import FormularioUsuario
from user.models import Usuario

# Create your views here.

class Login(FormView):
    template_name = 'user/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('home')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
			
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistroUsuario(CreateView):
	model = Usuario
	template_name = 'user/registro.html'
	form_class = FormularioUsuario
	success_url = reverse_lazy("login")