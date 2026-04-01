from django.shortcuts import render

# Create your views here.
# this rest paer is used in initial phase of apis
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
# @api_view()
# these are api decorators
# @api_view(['POST'])  we can give methods also to restrict 
# @api_view(['GET'])  we can give methods also to restrict 
# @api_view(['DELETE'])  we can give methods also to restrict 
# # @api_view(['POST'])  we can give methods also to restrict 
# def home(request):
#     return Response({'status':200 , 'message':'hello from django rest framework'})


from core.serializers import *
# this is api view 
# what is an api view
# api view is a kind of decorator which modifyies existing functionalyty of django function 
@api_view(['GET','POST','PUT','PATCH','DELETE'])  #Get method is used to serialized data can be displayed 
def home(request):
    if request.method=='GET':
        student_objs=Student.objects.all()
        serializer=STudentSerializer(student_objs,many=True)
        return Response({'status':200 , 'payload':serializer.data})
    elif request.method=='POST':
        data=request.data
        serializer=STudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('saved')
        return Response(serializer.errors)
    elif request.method=='PUT':
        data=request.data
        obj=Student.objects.get(id=data['id'])
        serializer=STudentSerializer(obj,data=data , partial=True)
        if serializer.is_valid():
            serializer.save()
            print('Puted')
        return Response(serializer.errors)
   
    elif request.method == 'PATCH':
        data=request.data
        obj=Student.objects.get(id=data['id'])
        serializer=STudentSerializer(obj,data=data , partial=True)
        if serializer.is_valid():
            serializer.save()
            print('saved')
        return Response(serializer.errors)
    else:
        data=request.data
        obj=Student.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'person deleted'})


@api_view(['GET','POST','PATCH'])
def Post_view(request):
    if request.method == 'GET':
        return Response({'ststuss':200,
                         'message':'yes! this is Get request in rest framework which you sent'
                         })
    elif request.method == 'POST':
        data=request.data
        print(data)
        return Response({'ststuss':200,
                         'message':'yes! this is POST request in rest framework which you sent'
                         })
    if request.method == 'PATCH':
        return Response({'ststuss':200,
                         'message':'yes! this is PATCH  request in rest framework which you sent'
                         })
    else:
        return Response({'status':200,'message':'you called invslid method'})



