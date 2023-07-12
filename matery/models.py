from django.db import models
from user.models import Usuario

# Create your models here.

class matery(models.Model):
	user=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	Matematicas1 = models.CharField(max_length=100, null=True)
	Matematicas2 = models.CharField(max_length=100, null=True)
	Matematicas3 = models.CharField(max_length=100, null=True)
	Matematicas4 = models.CharField(max_length=100, null=True)
	Matematicas5 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='materia'
		verbose_name_plural='materias'

	def __str__(self):
		return '{}'.format(self.Nombre)