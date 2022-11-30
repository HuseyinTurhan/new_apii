from django.contrib import admin
from .models import Users, Student

class UsersAdmin(admin.ModelAdmin):
   list_display = ('id','name','username','email','phone')

class StudentAdmin(admin.ModelAdmin):
   list_display = ('id','name','age','course','college')

admin.site.register(Student, StudentAdmin)
admin.site.register(Users, UsersAdmin)