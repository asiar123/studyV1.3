from django import forms

from person.models import Persona

class formularioPersona(forms.ModelForm):

	class Meta:
		model = Persona

		fields = [
			'edad',
			'carreraUniversitaria',
			'usuario',
			
		]
		labels = {
			'edad': '¿Cual es tu edad?:',
			'carreraUniversitaria': '¿Cual es tu carrera a seguir?:',
            'usuario': 'Seleccione su usuario',
			
		}
		widgets = {
            'edad': forms.TextInput(attrs={'class':'form-control'}),
			'carreraUniversitaria': forms.TextInput(attrs={'class':'form-control'}),
		}