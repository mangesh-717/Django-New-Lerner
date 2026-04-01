from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse('hello world for practice')
    people=[
        {'name':'dev','email':'mangeshsathe1353@gmail.com','education':'bsc','age':20},
    {'name':'raj','email':'raj@123.com','education':'btech','age':24},
    {'name':'duryodhan','email':'duryodhan@gmail.com','education':'lauda','age':34},
    {'name':'karn','email':'k@gmail.com','education':'phd','age':26},
    {'name':'bhima','email':'bhim@gmail.com','education':'phd','age':89},
    {'name':'ram','email':'rambhai@gmail.com','education':'everything','age':5000}]
    val={'peoples':people}
    return render(request,'index.html',val)

def basic(request):
    return render(request,'basic.html')


def second(request):
    return render(request,'second.html')