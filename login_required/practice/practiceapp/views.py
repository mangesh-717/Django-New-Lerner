# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .forms import student_info
# Create your views here.
from .models import Studentttt
@login_required
def index(request):
    
    return render(request,'index.html')


def login_form(request):
    if request.method == 'POST':
        form = student_info(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            name = form.cleaned_data['name']
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            photo = form.cleaned_data['photo']

            # Create and save the Student instance
            student_instance = Studentttt.objects.create(
                username=username,
                name=name,
                email=email,
                password=password,
                photo=photo
            )
            student_instance.save()
        else:
            print('Form is not valid')
    else:
        form = student_info()

    return render(request, 'login.html', {'form': form})




@login_required(login_url='login')
def result(request):
    data=Studentttt.objects.all()
    return render(request,'result.html' ,{'data':data})