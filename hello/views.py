from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view #for funtion based views
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status


def  front(request):
    return render(request, 'index.html')
@api_view(['GET', 'POST'])
def get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)  #api endpoint for fetching data
    elif request.method == 'POST':

        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  #save serializer to database
            return redirect('fetchdata')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #api endpoint to store data

@api_view(['DELETE', 'POST'])
def delete_student(request, pk):
    if request.method =='POST':
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return redirect('fetchdata')
    return redirect('fetchdata')


    

def fetchdata(request):
    import requests

    url = "http://127.0.0.1:8000/get_students/"  # your local API

    response = requests.get(url)
    data=response.json()
    return render(request, 'index.html', {'data':data})

#today is all about handling viewsets and routers viewsets handle crud operations automatically you dont need to use eg if request.method =='POST': etc evertime NB instead of writing 50 lines of code all CRUD operations can be done on a single class based view
#routers are written in views.py instead of using path('students/'.....) routers generates them

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
       
# Create your views here.
