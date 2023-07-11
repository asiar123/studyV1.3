from django.db import models

from user.models import Usuario

# Create your models here.

class Persona(models.Model):
	edad = models.CharField(max_length=50)
	carreraUniversitaria = models.CharField(max_length=70)
	usuario  = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    
	def __str__(self):
		return '{}'.format(self.usuario)