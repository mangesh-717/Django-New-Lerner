from django.shortcuts import render,redirect
from crudapp.models import Contact


from django.contrib import messages                              #its for showing messages in web
# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        stname=request.POST['stname']
        phone=request.POST['phone']
        age=request.POST['age']
        email=request.POST['email']
        content=request.POST['content']
        age = int(age) if age.isdigit() else None if age == '' else age

        if len(name)>=3 and len(email)>3 and len(phone)>=10 and len(content)>2:
            # messages.error(request,'please fill the form currectly')  
            contact=Contact(name=name , lastname=lastname , stname=stname ,phone=phone,age=age ,email=email ,content=content)
            
            contact.save()
            print('its not acceptable')
            contacts = Contact.objects.all()

            return render(request,'result.html',{'contacts': contacts})  # Redirect to the next HTML page

        else:
            
            messages.error(request,'please fill the form currectly')  

        
            

    return render(request,'index.html')




from .utils import send_email_v


from django.db.models import Count,Sum,Avg,Min,Max,StdDev,Variance
def result(request):
    data=Contact.objects.values().reverse()
    result =Contact.objects.annotate(Count('age'))
    for i in result:
        print(i)
    print(result)
    # send_email_v(request)
    




   
    return render(request,'result.html',{'data':data})


    # return render(request, 'sms_sent.html')


