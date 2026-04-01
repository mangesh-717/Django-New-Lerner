from django.shortcuts import render


def index(request):
# data can be passed in temples by dictionary also 
    params={'name':'dev','place':'Mars'}

    return render(request,'index.html' , params)