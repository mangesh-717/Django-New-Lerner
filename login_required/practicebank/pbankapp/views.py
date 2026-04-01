from django.shortcuts import render,redirect
from .models import Bankusers,CardApplication,HelpData,LoanRequest,Transaction
from django.contrib.auth.models import User
from .forms import loginform,LoanRequestForm,HelpDesk

# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import Bankusers
from django.contrib.auth.models import User
from django.contrib import messages
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        lastname=request.POST['lastname']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        account_type=request.POST['account-type']
        adhar_card=request.FILES['aadhar-card']
        photo=request.FILES['photo']
        if User.objects.filter(username=username):
            messages.error(request,'⚠️ username already exists go for login')
            print('problem')
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, first_name=name, last_name=lastname)
        user.set_password(password)
        bank_user = Bankusers.objects.create(
            account_type=account_type,
            phon=phone,
            photo=photo,
            adhar=adhar_card
        )
        bank_user.save()
        user.save()
        messages.success(request,'user has been succesfully created \n login now')
    return render(request,'register.html')





from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def login_form(request):
    use=None
    form=loginform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username= form.cleaned_data['username']
            email= form.cleaned_data['Email']
            password = form.cleaned_data['password']
            if not(User.objects.filter(username=username).exists()):
                messages.error(request,"!!.⚠️username does't match")
            else:
                use=authenticate(username=username,password=password)
            if use is None:
                messages.error(request,"⚠️!Invalid Password")
                return redirect("loginform")
            else:
                login(request,use)
                request.session['logged_in_once'] = True  # Set session variable
                messages.success(request, 'Logged in successfully! \n Now you can to your Section')
    form=loginform()
    return render(request,'login.html',{'form':form})

# @login_required(login_url='loginform')
# def operations(request):
#     # if not request.user.is_authenticated:
#     if request.user.is_authenticated and request.session.get('logged_in_once'):
#         return render(request, 'operations.html')
#     else:
#         return redirect('loginform')
#         # return redirect('loginform')
#     # return render(request,'operations.html')
def result(request):

    return render(request,'result.html')


def help(request):
    if request.method == 'POST':
        form = HelpDesk(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Issue has been submitted successfully!')
    form=HelpDesk()
    return render(request,'help.html',{'form':form})



def creadit_debit(request):
    return render(request,'creadit_debit.html')

# from .forms import CardApplicationForm  # Import your form class here
from django.contrib import messages
@login_required(login_url='loginform')
def creadit_debit_form(request):
    if request.method == 'POST':
        user = request.user
        email=request.POST['email']
        debit_card = 'debit' in request.POST
        credit_card ='credit' in request.POST

        if user.email==email:
            # return redirect('home')  # Redirect to the dashboard or any other page
            if CardApplication.objects.filter(user=user).exists():
                if CardApplication.objects.filter(user=user, creaditcard=True).exists() and CardApplication.objects.filter(user=user, debitcard=True).exists():
                    messages.error(request, 'You have already applied for Both cards. Go to Help Section')
                    # return redirect('help')
                else:
                    card_application = CardApplication.objects.get(user=user)
                    if card_application.debitcard==False and debit_card==True:
                        card_application.debitcard = debit_card
                        card_application.save()

                        messages.success(request, 'debit Card application submitted successfully!')
                    if card_application.creaditcard==False and credit_card==True:
                        card_application.creaditcard = credit_card
                        card_application.save()
                        messages.success(request, 'Credit Card application submitted successfully!')

                    if card_application.debitcard==True and debit_card==True or card_application.creaditcard==True and credit_card==True:
                        if debit_card:
                            messages.error(request, '⚠️You have already applied for a debit card.')
                        if credit_card:
                            messages.error(request, '⚠️You have already applied for a credit card.')
    
            else:
                card_application = CardApplication.objects.create(
                user=user,
                creaditcard=credit_card,
                debitcard=debit_card
              )
                card_application.save()
                messages.success(request, 'Card application submitted successfully!')
        else:
            messages.error(request, "⚠️Enter email correctly")
    return render(request,'creadit_form.html')

@login_required(login_url='loginform')
def loan_request_view(request):
    if request.method == 'POST':
        user = request.user
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['Username']
            email= form.cleaned_data['email']
            amount = form.cleaned_data['amount']
            Loan_Tenure= form.cleaned_data['Loan_Tenure']
            purpose = form.cleaned_data['purpose']
            message = form.cleaned_data['message']
        if LoanRequest.objects.filter(user=user).exists():
            messages.error(request, 'You have already applied for Loan So go to help desk')
        else:
            if user.email==email and user.username==username:
                loan_application= LoanRequest.objects.create(
                        user=user,
                        amount=amount,
                        Loan_Tenure=Loan_Tenure,
                        purpose=purpose,
                        message=message
                      )
                loan_application.save()
                messages.success(request, 'Loan application submitted successfully!')
    
            else:
                messages.error(request, "⚠️Enter username and email correctly")
    else:
        form = LoanRequestForm()
    return render(request,'loan.html', {'form': form})


@login_required(login_url='loginform')
def account(request):
    from django.core.exceptions import ObjectDoesNotExist
   
    try:
        user=request.user
        # print(user.username,user.id)
        # print(user.first_name,user.email,user.id,user.username)
        # user_aa = User.objects.all()
        # for user_a in user_aa:
        #     print(user_a.first_name,user_a.last_name,user_a.email,user_a.username,user_a.id)

       

        useruser = User.objects.get(id=3)
        bank_user = Bankusers.objects.get(id=3) 
        transaction = Transaction.objects.create(
            user=useruser,
            bank_user=bank_user,
            Credited=100.00, 
            Debited=.00,    
            Transferred='deposit',  
            emi=None  
        )
        transaction.save()
            
        # transactions=Transaction.objects.all()
        # for i in transactions:
        #     print(i.Credited,i.Debited,i.user,i.bank_user)
        print('succied')
        user_account = Bankusers.objects.all()
        for i in user_account:
            print(i.account_number,i.current_balance,i.id)
        

        # # name=user.first_name
    except Bankusers.DoesNotExist:
        print("doesn't fount")
    #     # messages.error(request, 'User account not found.')
    # if request.method == 'POST': 
    #     user=request.user
    #     credit_amount=request.POST.get('creditAmount')
    #     debit_amount = request.POST.get('debitAmount')
    #     transferAmount=request.POST.get('transferAmount')
    #     recipientemail=request.POST.get('recipientEmail')
    #     recipientAccountNo=request.POST.get('recipientAccount')
    #     if 'Emipayed' in request.POST:
    #         print('True')

       
    #     if dbalance>=float(transferAmount):
    
    #         try:
    #             if Bankusers.objects.get(account_number=recipientAccountNo).id == User.objects.get(email=recipientemail).id and user.email != recipientemail :
    #                 pkid=Bankusers.objects.get(account_number=recipientAccountNo) 
    #                 previous=pkid.current_balance
    #                 if int(transferAmount)>0:
    #                     pkid.current_balance=previous+int(transferAmount)
    #                     pkid.save()
    #                     # mail updation should be given here to amount resiver

    #                     transfered=dbalance-int(transferAmount)
    #                     user_account.current_balance=transfered
    #                     # mail updation should be given here to amount sender

    #                     messages.success(request, 'Money has been transfered suceesfully.')
    #                 else:
    #                     messages.error(request, 'Enter amount in positive.')
    #         except Bankusers.DoesNotExist:
    #             messages.error(request, 'Invalid account number or email.')
    #     else:
    #         messages.error(request, 'Entered Transfer Amount is greater than Your Balance.')
     
    # data=Bankusers.objects.all()
    return render(request,'operations.html')

def About(request):
    return render(request,'about.html'
                  
                  )
@login_required(login_url='loginform')
def carrier(request):
    # next_url = request.GET.get('next', None)
    # if request.user.is_authenticated:
    #     # If 'next' is present, redirect to that URL after login
    #     if next_url:
    #         return redirect(next_url)
    #     else:
    #         return render(request, 'join-our-tem.html')
    # else:
    #     # User is not authenticated, they will be redirected to the login page
    #     return render(request, 'loginform.html')
    return render(request,'join-our-tem.html')