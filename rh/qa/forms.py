from django import forms
from .models import Qa

class QaForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = Qa
		fields = ('first','last','email','password', 'age')