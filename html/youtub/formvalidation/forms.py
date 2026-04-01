from django import forms
from . models import Employee

class Employee_Form(forms.ModelForm):


    class Meta:
        model=Employee
        fields=('fullname','mobile','emp_code','position')
        # filds='__all__'
        

        lables={'fullname':'Full. Name' ,
                'emp_code':'EMP. Code:'}
        



    # its for that selection option 
    def __init__(self,*args,**kwargs):
        super(Employee_Form,self).__init__(*args, **kwargs)
        self.fields['position'].empty_lable='select'
        self.fields['emp_code'].required=False
        self.fields['mobile'].required=False




# form can be made like this also
class UpdateInformationForm(forms.Form):
    position = forms.ChoiceField(choices=[('developer', 'Developer'), ('designer', 'Designer'), ('manager', 'Manager')])
    name = forms.CharField()
    phon = forms.IntegerField()
    