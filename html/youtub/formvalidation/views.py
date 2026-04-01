from django.shortcuts import render,redirect
from .forms import Employee_Form,UpdateInformationForm
from .models import Employee
# Create your views here.
def employee_form(request):
    if request.method=='GET':
        form=Employee_Form()
        return render(request,'employee_form.html',{'form':form})
    else:
        form=Employee_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list/')


def employee_list(request):
    context=Employee.objects.all()

    return render(request,'employee_list.html',{'records':context})


def employee_delete(request,id):
    queryset=Employee.objects.get(id=id)
    
    print(queryset.id)
    # queryset.delete()
    return redirect('_list')


def updation_data(request,id):
    idno=Employee.objects.get(id=id)
    form = UpdateInformationForm(request.POST)
    if form.is_valid():
            # Process the form data
            position = form.cleaned_data['position']
            name = form.cleaned_data['name']
            phon = form.cleaned_data['phon']
            print(name,phon,position)

    if request.method == 'POST':
        # name = request.POST.get('name')
        # phon = request.POST.get('Phon')
        
        # it can't be updated becaus foraign key relationship is here
        # position = request.POST.get('position')
    # Your processing logic goes here
        # print(name,phon,position)
        if name:
            idno.fullname=name
        if phon:
            idno.mobile=phon
        # if position:
            # idno.position=position
        idno.save()
        return redirect('_list')
    form = UpdateInformationForm()

    return render(request, 'base.html',{'form':form})

