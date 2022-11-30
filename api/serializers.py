from rest_framework import serializers
from .models import Student, Users

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "age", "course", "college"]

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["id", "name", "username", "email","phone"]