from django import forms

from matery.models import matery

class FormMatery(forms.ModelForm):

	class Meta:
		model = matery

		fields = [
			'user',
			'Matematicas1',
			'Matematicas2',
			'Matematicas3',
			'Matematicas4',
			'Matematicas5',
			
		]
		labels = {
			'user': 'Seleccione su usuario',
			'Matematicas1': '¿Que son los números naturales?',
			'Matematicas2': '¿Que son los números enteros?',
			'Matematicas3': '√432',
			'Matematicas4': '2918838/897',
			'Matematicas5': '(45/26)*(39/25)*(22/33)',
			
		}
		widgets = {
			'Matematicas1': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas2': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas3': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas4': forms.TextInput(attrs={'class':'form-control'}),
			'Matematicas5': forms.TextInput(attrs={'class':'form-control'}),
		}