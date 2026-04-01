# from django.shortcuts import render
# # Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from .forms import studentform,UpdateInformationForm,loginform,register
from .models  import student
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def index(request):
   
    if request.method == "POST":
        form = studentform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            success=False
    else:
        form =studentform()
    return render(request,"index.html",{"form":form})

# @login_required
def result(request):
    data = student.objects.all()
    return render(request,'result.html',{"data":data})

def delete(request,id):
    student.objects.get(id=id).delete()
    return redirect('result')




def update(request, id):
    data = student.objects.get(id=id)
    form =UpdateInformationForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            name = form.cleaned_data['name']
            phon = form.cleaned_data['email']
            details = form.cleaned_data['about']
            if name:
                data.name=name
            if phon:
                data.email=phon
            if details:
                data.about=details
            data.save()
            return redirect('result')
    form=UpdateInformationForm()
    return render(request,"update.html",{"form":form})
   



# to confirm the encriptead password we need to import django contrib auth authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def login_form(request):

    form=loginform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']
            # print(username,password)
            # val=User.objects.all()
            # for i in val:
            #     print(i.username,i.password,i.first_name)


            # user=User.objects.filter(username=username)
            # if not(user.exists()):
                # print("it doesn't match ")
            if not(User.objects.filter(username=username).exists()):
                messages.error(request,"username does't match")
                return redirect("login")
            else:
                print('it matched')
            
            use=authenticate(username=username,password=password)
            if use is None:
                messages.error(request,"Invalid Password")
                return redirect("/login/")
            else:
                login(request,use)
                return redirect('/add_info/')


    form=loginform()     
    return render(request,'login.html',{'form':form})
def log_out(request):
    from django.contrib.auth import logout

    logout(request)
    return redirect('/login/')
def register_form(request):
    form=register(request.POST)
    if request.method == 'POST':
        if form.is_valid():
# if user name is already exist then it will through error            # 
            username= form.cleaned_data['username']
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['Last_name']
            password = form.cleaned_data['userpassword']

# to check user is exists or not
            user_banck=User.objects.filter(username=username)
            # to give error message on form we need to import messages from django.contrib
            from django.contrib import messages
            if user_banck.exists():
                messages.error(request,'username already exists go for login')
                return redirect('/register/')


            us=User.objects.create(username=username,first_name=first_name,last_name=last_name)
            us.set_password(password)
            us.save()
            messages.success(request,'user has been succesfully created ')

            return redirect('/register/')
    form=register()
    return render(request,'register.html',{'form':form})