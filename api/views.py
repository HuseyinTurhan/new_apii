from django.shortcuts import render
from django.http import JsonResponse
from .models import Users, Student
from django.views.generic import ListView,DetailView
from rest_framework.decorators import api_view
from rest_framework import generics
from api.serializers import StudentSerializer, UsersSerializer


class UsersListView(ListView): 
    queryset = Users.objects.all()
    context_object_name = "userinfo"

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UsersDetail(generics.RetrieveDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer