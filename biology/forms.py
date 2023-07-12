from django import forms

from biology.models import Biology

class FormBiology(forms.ModelForm):

	class Meta:
		model = Biology

		fields = [
			'usuario',
			'Biology1',
			'Biology2',
			'Biology3',
			'Biology4',
			'Biology5',
			'Biology6',
			'Biology7',
			'Biology8',
			'Biology9',
			'Biology10',
			
		]
		labels = {
			'usuario': '¿Usuario?',
			'Biology1': '¿Significado de masa?',
			'Biology2': '¿Que es volúmen?',
			'Biology3': 'Estado solido (ejemplo)',
			'Biology4': 'Estado gas (ejemplo)',
			'Biology5': 'Estado liquido (ejemplo)',
			'Biology6': 'Significado de carbohidratos:',
			'Biology7': '¿Cuales son los tipos de proteinas?',
			'Biology8': '¿Principales diferencias entre celula eucariota y procariota?',
			'Biology9': '¿Como ocurre el transporte celular?',
			'Biology10': 'Cuales son las principales caracteristicas de las fases Mitosis y Meiosis',
			
		}
		widgets = {
			'Biology1': forms.TextInput(attrs={'class':'form-control'}),
			'Biology2': forms.TextInput(attrs={'class':'form-control'}),
			'Biology3': forms.TextInput(attrs={'class':'form-control'}),
			'Biology4': forms.TextInput(attrs={'class':'form-control'}),
			'Biology5': forms.TextInput(attrs={'class':'form-control'}),
			'Biology6': forms.TextInput(attrs={'class':'form-control'}),
			'Biology7': forms.TextInput(attrs={'class':'form-control'}),
			'Biology8': forms.TextInput(attrs={'class':'form-control'}),
			'Biology9': forms.TextInput(attrs={'class':'form-control'}),
			'Biology10': forms.TextInput(attrs={'class':'form-control'}),
		}