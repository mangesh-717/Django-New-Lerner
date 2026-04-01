from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    response=requests.get('https://jsonplaceholder.typicode.com/users')
    results=response.json()
    return render(request,'index.html',{'results':results})



def countries(request):
    response=requests.get('https://restcountries.com/v2/all')
    data=response.json()
    return render(request,'countries.html',{'data':data})