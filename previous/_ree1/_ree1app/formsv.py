from django import forms
from _ree1app.models import Student

class user_form(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"