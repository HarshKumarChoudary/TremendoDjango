from django.contrib import admin
from .models import student,teacher,batch,profile

@admin.register (profile)
class profile_admin(admin.ModelAdmin):
    list_display = ['id','user','is_verified','auth_token']

@admin.register (student)
class student_admin(admin.ModelAdmin):
    list_display = ['id','profile','name','address','email','gender','photo']

@admin.register (teacher)
class teacher_Admin(admin.ModelAdmin):
    list_display = ['id','profile','name','address','phone_no','email','photo']

@admin.register (batch)
class batch_admin(admin.ModelAdmin):
    list_display = ['id','Teacher','Student','totalclasses','completedclasses']