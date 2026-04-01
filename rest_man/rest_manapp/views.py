from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_manapp.serializer import studentSerializer
from .models import student
@api_view(['GET'])
def get_student(request):
    response={'status':200}
    student_objs=student.objects.all()
    serilizer=studentSerializer(student_objs,many=True)
    response['data']=serilizer.data
    return Response(response)

from rest_framework import status

@api_view(['POST'])
def post_student(request):
    data = request.data
    print(data)
    serializer = studentSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        response = {
            'status': 200,
            'data': serializer.data,
            'message': 'Student created successfully'
        }
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {
            'status': 400,
            'errors': serializer.errors,
            'message': 'Student creation failed'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','PATCH'])
def home(request):  
    response={'statjv':'dfv','vfvfdv':'vdfvd'}
    if request.method=='GET':
        print("get")
    else:
        print('post')
    return Response(response)