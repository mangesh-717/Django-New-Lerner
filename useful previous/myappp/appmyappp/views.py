from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'name':'Sultan',
             'cities':['mumbai','pune','dubaiphata'],
             'std_details':({'name':'ramesha','age':21,'marks':65,'degree':'BE','stream':'CS'},
                            {'name':'suresha','age':23,'marks':70,'degree':'BCA','stream':'CA'},
                            {'name':'rambha','age':33,'marks':90,'degree':'IIT','stream':'SE'},
                            {'name':'paru','age':30,'marks':40,'degree':'BSC','stream':'MACHENICAL'},
                            )}
           
    return render(request,'index.html',context=my_dict)
