from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer


class employeeList(APIView):
    
    def get(self,request):
        employeesl= employees.objects.all()
        serializer=employeesSerializer(employeesl, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass