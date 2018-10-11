from django import forms

from .models import Contactos

class ContactoForm(forms.ModelForm):

	class Meta:
		model = Contactos
		fields = ('telefono', 'email', 'mensaje',)
