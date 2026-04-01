from django import forms

from .models import Studentttt
class student_info(forms.Form):
    
    # class Meta:
    #     model = Studentttt
    #     fields = "__all__"
    name=forms.CharField()
    user_name=forms.CharField()
    password = forms.CharField( widget=forms.PasswordInput)
    email=forms.EmailField()
    photo=forms.FileField(required=True)
