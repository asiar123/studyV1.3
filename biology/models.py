from django.db import models
from person.models import Persona

# Create your models here.

class Biology(models.Model):
	usuario=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	Biology1 = models.CharField(max_length=100, null=True)
	Biology2 = models.CharField(max_length=100, null=True)
	Biology3 = models.CharField(max_length=100, null=True)
	Biology4 = models.CharField(max_length=100, null=True)
	Biology5 = models.CharField(max_length=100, null=True)
	Biology6 = models.CharField(max_length=100, null=True)
	Biology7 = models.CharField(max_length=100, null=True)
	Biology8 = models.CharField(max_length=100, null=True)
	Biology9 = models.CharField(max_length=100, null=True)
	Biology10 = models.CharField(max_length=100, null=True)

	class Meta:
		verbose_name='biology'
		verbose_name_plural='biologys'

	def __str__(self):
		return '{}'.format(self.usuario)