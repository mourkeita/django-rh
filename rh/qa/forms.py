from django import forms
from .models import Employee, Company, Employment, Relationship, CompanyInformations

class EmployeeForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	age = forms.IntegerField(min_value=0, max_value=200)
	class Meta:
		model = Employee
		fields = ('first','last','email','password', 'age', 'avatar', 'friends')


class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name', 'address', 'telephone', 'siren', 'siret', 'activity', 'size')


class CompanyInformationsForm(forms.ModelForm):
	class Meta:
		model = CompanyInformations
		fields = ('company', 'category', 'state', 'country', 'city')


class EmploymentForm(forms.ModelForm):
	class Meta:
		model = Employment
		exclude = ('Employee', 'Company')

class RelationshipForm(forms.ModelForm):
	class Meta:
		model = Relationship
		fields = ('sender',)