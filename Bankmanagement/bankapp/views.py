from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
# from .forms import form_info
# from .models import bankUsers
# # Create your views here.   
# from django.contrib import messages
# def login_form(request):
#     if request.method == 'POST':
#         form = form_info(request.POST, request.FILES)
#         if form.is_valid():
#             name=form.cleaned_data['name']
#             photo=form.cleaned_data['photo']
#             email=form.cleaned_data['email']
#             us=bankUsers.objects.create(name=name,photo=photo,email=email)
#             us.save()
#             messages.success(request, 'Form submitted successfully')  # Add a success message
#             # data=Users.objects.all()
#             # return render(request,'result.html',{'data':data}) # Redirect to the 'result' page after successful form submission


#         else:
#             messages.error(request, 'Form submission failed. Please check the form.')
#     else:
#         form = form_info()

#     return render(request, 'index.html', {"form": form})




# from django.contrib.auth.decorators import login_required
# @login_required
# def result(request):
#     data=bankUsers.objects.all()
#     return render(request,'result.html',{'data':data})
