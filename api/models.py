from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
