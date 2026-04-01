from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):

    #Getting the data into html page  
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse(f"""<h3>Removepunc is the second pipe of view which is called in urls { djtext }</h3>""")





def capitalizefirst(request):
    return HttpResponse("""'<h3>Capitalizefirst is the third pipe of view which is called in urls </h3>""")

def newlineremove(request):
    return HttpResponse("""'<h3>Newlineremove is the fourth second pipe of view which is called in urls </h3>""")

def Spaceremove(request):
    return HttpResponse("""'<h3>Spaceremove is the fifth pipe of view which is called in urls </h3>""")

def charcount(request):
    return HttpResponse("""'<h3>Charcount is the sixth pipe of view which is called in urls </h3>""")


