from django import forms
from .models import Qa

class QaForm(forms.ModelForm):
	class Meta:
		model = Qa
		fields = ('first','last','email','password', 'age')