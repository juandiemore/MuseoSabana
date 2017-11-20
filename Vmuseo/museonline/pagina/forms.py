from django import forms
from .models import obra

class ObraForm(forms.ModelForm):
	class Meta:
		model = obra
		fields = '__all__'

