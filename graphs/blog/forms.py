from django import forms
from django.forms import ModelForm

from .models import User


class GraphForm(ModelForm):
	class Meta:
		model=User
		fields=['name','type_Of_Graph','x_Attribute','y_Attribute','file_csv']
