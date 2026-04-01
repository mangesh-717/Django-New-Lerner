from django.shortcuts import render
from formsapp.forms import EmployeeForm

from django.http import HttpResponse 
# Create your views here.
def index(request):
    form=EmployeeForm()

    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            print('Validation success')
            print(form.cleaned_data['name'])
            print(form.cleaned_data['salary'])
            print(form.cleaned_data['phone'])
            print(form.cleaned_data['address'])
        return HttpResponse('<h1> Validation successed</h1>')

    return render(request,'index.html',{'mangesh':form})

