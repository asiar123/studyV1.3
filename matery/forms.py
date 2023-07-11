from django import forms

from matery.models import matery

class FormMatery(forms.ModelForm):

	class Meta:
		model = matery

		fields = [
			'user',
			'Nombre',
			'Orientacion1',
			'Orientacion2',
			'Orientacion3',
			'Orientacion4',
			'Orientacion5',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Nombre': 'Nombre de la materia',
			'Matematicas1': '¿Que son los números naturales?',
			'Matematicas2': '¿Que son los números enteros?',
			'Matematicas3': '√432',
			'Matematicas4': '2918838/897',
			'Matematicas5': '(45/26)*(39/25)*(22/33)',
			
		}
		widgets = {
			'Nombbre': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion1': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion2': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion3': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion4': forms.TextInput(attrs={'class':'form-control'}),
			'Orientacion5': forms.TextInput(attrs={'class':'form-control'}),
		}