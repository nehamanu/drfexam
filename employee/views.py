from functools import partial

from django.shortcuts import render,get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from employee.models import Employee
from employee.permissions import IsOwner
from employee.serializers import EmployeeSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    def post(self, request):
        serializer_instance = EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)

    def get(self,request):
        qs=Employee.objects.all()
        serializer_instance=EmployeeSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

class RetrieveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwner]
    def get(self,request,id):
        e=get_object_or_404(Employee,id=id)
        serializer_instance=EmployeeSerializer(e)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        e= get_object_or_404(Employee, id=id)
        self.check_object_permissions(e,request)
        serializer_instance =EmployeeSerializer(e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        e= get_object_or_404(Employee, id=id)
        self.check_object_permissions(e,data=request.data,partial=True)
        serializer_instance =EmployeeSerializer(e)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(data=serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        e =Employee.objects.get(id=id)
        self.check_object_permissions(e,request)
        e.delete()
        return Response({"message":"Deleted Successfully"})

class RegisterAPIView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def get(self,request):
        print(self.request.user)
        self.request.user.auth_token.delete()
        return Response({'message':'Logout successfully'})
