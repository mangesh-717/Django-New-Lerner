
from django.shortcuts import render
from _ree1app.formsv import user_form
from _ree1app.models import Student
# Create your views here.
def index(request):
    form=user_form()
    if request.method=='POST':
        form=user_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"index.html",{'form':form})

def display(request):
    images=Student.objects.all()
    return render(request,"display.html",{'images':images})
def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')
def carrier(request):
    return render(request,'carrier.html')