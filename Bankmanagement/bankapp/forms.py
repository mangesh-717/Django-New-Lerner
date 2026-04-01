from django import forms
# from .models import bankUsers
class form_info(forms.Form):



# class register(forms.Form):
    name=forms.CharField()
    photo=forms.FileField()
    email= forms.EmailField()