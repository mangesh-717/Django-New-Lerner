from django import forms
class EmployeeForm(forms.Form):
    name=forms.CharField(max_length=100)
    emp_id=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.IntegerField()
    address=forms.CharField(max_length=100)
    salary=forms.IntegerField()
