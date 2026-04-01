from django import forms
from .models import student
class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"

class loginform(forms.Form):
    username= forms.CharField()
    password= forms.CharField(widget=forms.PasswordInput)


class register(forms.Form):
    first_name=forms.CharField()
    Last_name=forms.CharField()
    username= forms.CharField()
    userpassword= forms.CharField(widget=forms.PasswordInput)
    

class UpdateInformationForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    about=forms.CharField()

    # fields =('name','email')
        # fields = ["name","email"]
    
