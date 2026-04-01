from django.shortcuts import render,get_object_or_404

# # Create your views here.
from .models import studentdata

# # Create your views here.
def index(request):
    if request.method=='POST':
        data=request.POST
        name=request.POST['name']
        last_name=request.POST['lname']
        age=request.POST['age']
        phon=request.POST['phon']
        email=request.POST['email']
        photo=request.FILES.get('photos')
        students.objects.create(name=name, last_name=last_name,age=age , phon=phon, email=email,photo=photo)
        print('succed')
        print(photo)
    return render(request,'index.html')

def result(request):
    
    contacts = student.objects.all().order_by('name')
    return render(request,'result.html')#,{'contacts': contacts})










# # def updation(request):
    
# #     # if request.method=='POST':
# #     #     old_email_id=request.POST['identifier'] #it will take email or idcode
# #     #     new_phon=request.POST.get('new_phon',None)
# #     #     new_email=request.POST.get('new_email',None)
# #     #     new_name=request.POST.get('new_name',None)
# #     #     new_lastname=request.POST.get('new_lastname',None)
# #     #     age=request.POST.get('new_age',None)
# #     #     selected_option = request.POST.get('radio_group')

        
# #     #     if selected_option == 'option1':
# #     #         contacts = student.objects.get(id=old_email_id)
# #     #         if new_phon!=None:
# #     #             contacts.phon=new_phon
# #     #         if new_email!=None:
# #     #             contacts.email=new_email
# #     #         if new_name!=None:
# #     #             contacts.name=new_name
# #     #         if new_lastname!=None:
# #     #             contacts.last_name=new_lastname
# #     #         if age!=None:
# #     #             contacts.age=age
# #     #     elif selected_option == 'option2':
# #     #         contacts = student.objects.get(mail=old_email_id)
# #     #         if new_phon!=None:
# #     #             contacts.phon=new_phon
# #     #         if new_email!=None:
# #     #             contacts.email=new_email
# #     #         if new_name!=None:
# #     #             contacts.name=new_name
# #     #         if new_lastname!=None:
# #     #             contacts.last_name=new_lastname
# #     #         if age!=None:
# #     #             contacts.age=age
# #     #     contacts.save()
# #     return render(request,'updation.html')



# # def deleation(request):
#     return render(request ,'deletion.html')