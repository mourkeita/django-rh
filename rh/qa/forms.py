from django import forms
from .models import Qa, Company

class QaForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	age = forms.IntegerField(min_value=0, max_value=200)
	class Meta:
		model = Qa
		fields = ('first','last','email','password', 'age', 'avatar')


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name', 'address', 'telephone', 'siren', 'siret', 'activity', 'size')