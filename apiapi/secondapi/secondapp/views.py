from django.shortcuts import render
from django.http import JsonResponse
from .models import Students


from .serializations import StudentSerializing
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

# here if list is there then safe=false must be done 
def index_(request):
    pass
    l1={'mangesh':'dada','sathe':'tate'}
    return JsonResponse(l1)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def serializedatudent(request):
    if request.method=='GET':
        student_data=Students.objects.all()
        serializedatudentdata=StudentSerializing(student_data,many=True)
        return Response(serializedatudentdata.data)
    elif request.method=='POST': 
        data=request.data
        serialization=StudentSerializing(data=data)
        if serialization.is_valid():
            serialization.save()
            print('saved')
        return Response(serialization.errors)
    elif request.method == 'PUT':
        data=request.data
        obj=Students.objects.get(id=data['id'])
        serialization = StudentSerializing(obj, data=data)
        if serialization.is_valid():
            serialization.save()
            print('updated')
        return Response(serialization.errors)
    elif request.method == 'PATCH':
        data=request.data
        obj=Students.objects.get(id=data['id'])
        serilization=StudentSerializing(obj,data=data,partial=True)
        if serilization.is_valid():
            serilization.save()
            print('patched')
        return Response(serilization.errors)
    elif request.method == 'DELETE':
        data=request.data
        obj=Students.objects.get(id=data['id'])
        obj.delete()
        return Response({'message':'Student deleted'})
    else:
        return Response({'message':'Invalidoptions'})





# in order to work with apiview we need to import restframework.views apiview which is use to code can be reduced
from rest_framework.views import APIView
class PersonApi(APIView):
    def get(self,request):
        return Response({"message":"This is a get method Request"})
    def post(self,request):
        return Response({"message":"This is a Post method Request"})
    def put(self,request):
        return Response({"message":"This is a Put method Request"})
    def patch(self,request):
        return Response({"message":"This is a Patch method Request"})
    def delete(self,request):
        return Response({"message":"This is a Delete method Request"})
    


#django rest fremwork has class thats cauled model view set which is capebel of handaling all the crud operations in just two lines of code 
from rest_framework import viewsets
# we need to focus on application layer 
class StudentViewset(viewsets.ModelViewSet):
    serializer_class=StudentSerializing
    queryset=Students.objects.all()

    # if we want to perform specific methods on model view set when we have to use http_method_name=
    http_method_names=['POST','GET']



    # search functionality
    def list(self,request):
        search=request.GET.get('search')
        queryset=self.queryset
        if search:
            queryset = queryset.filter(name__startswith=search)

        serializer=StudentSerializing(queryset,many=True)
        return Response({"status":200,"data":serializer.data})
    
    # but for searching we need to give this path 
    # http://127.0.0.1:8000/students/students/?search=m


    
    # actions in django it is used only on viewsets means model viewsets
    from rest_framework.decorators import action   
    # it is one type of decorator 
    
    @action(detail=False , methods=['POST'])
    def send_email_to(self,request):
        return Response({'message':'email sent succesfully'        })
