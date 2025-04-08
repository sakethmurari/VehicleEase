from .models import Login
from django import forms

class loginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'