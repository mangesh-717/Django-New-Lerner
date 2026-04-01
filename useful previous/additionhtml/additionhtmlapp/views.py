from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    n1=int(request.POST['num1'])
    n2=int(request.POST['num2'])
    
    
    if 'addition' in request.POST:
        res=n1+n2
    if 'substract' in request.POST:
        res=n2-n1
    if 'multiplication' in request.POST:
        res=n1*n2
    if 'division' in request.POST:
        res=n1/n2
    if 'mod' in request.POST:
        res=n1%n2


   
    return render(request,'result.html',{'res':res})

