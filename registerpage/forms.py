from .models import Register
from django import forms

class registerForm(forms.ModelForm):
    class Meta:
        model=Register
        fields='__all__'