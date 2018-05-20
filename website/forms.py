from django import forms

from .models import UserData

class CreateForm(forms.Form):
	name      = forms.CharField()
	company   = forms.CharField(required=False)
	email 	  = forms.CharField(required=False)
	comment   = forms.CharField(required=False)

class UserDataCreateForm(forms.ModelForm):
	class Meta:
		model = UserData
		fields = [
			'name',
			'company',
			'email',
			'comment'
			]