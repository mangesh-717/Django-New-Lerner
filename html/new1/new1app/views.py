from django.shortcuts import render,HttpResponse,redirect
from .forms import studentform,UpdateInformationForm
from .models  import student
# Create your views here.
def index(request):
    success=False
    if request.method == "POST":
        form = studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success="your data stired succesfully"
        else:
            success=False
            return HttpResponse("data was not saved")
    else:
        form =studentform()
    data = student.objects.all()
    return render(request,"index.html",{"form":form ,"success_message":success})



def update(request, id):

    data = student.objects.get(id=id)
    
    # form = updateform(request.POST , request.FILES , instance=data )
    form =UpdateInformationForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            name = form.cleaned_data['name']
            phon = form.cleaned_data['email']
            print(name,phon)
    #       
            if name:
                data.name=name
            if phon:
                data.email=phon
            data.save()
            return redirect('result')

    #     else:
    #         return HttpResponse("data was not saved")
    
    # else:
    
    form=UpdateInformationForm()

    return render(request,"update.html",{"form":form})
    # return render(request,"update.html",{"form":form,"data":data})
    # pass

def result(request):

    data = student.objects.all()

    return render(request,'result.html',{"data":data})

