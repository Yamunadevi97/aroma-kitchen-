from django import forms
from suggestion.models import cus
class cusModelForm(forms.ModelForm):
  class Meta:
   model=cus
   fields='__all__'


