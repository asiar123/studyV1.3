from django.contrib import admin
from user.models import Usuario
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Usuario) 
admin.site.register(Permission)