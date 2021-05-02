from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100,default=0,null=True)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return (self.user.username)

class student(models.Model):
    gender_list=[
    ('M','male'),
    ('F','female'),
    ]
    profile = models.ForeignKey(profile, on_delete=models.CASCADE,default=0,null=True)
    name = models.TextField(null=True)
    address = models.TextField(null=True)
    gender = models.CharField(max_length=6,choices=gender_list,null=True)
    email = models.EmailField(max_length=250,null=True)
    photo = models.ImageField(upload_to="img",null=True)
    #batchenrolled = models.ForeignKey("batch",on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.id)
    

class teacher(models.Model):
    profile = models.ForeignKey(profile, on_delete=models.CASCADE,default=0)
    name = models.TextField(null=True)
    address = models.TextField(null=True)
    phone_no = models.IntegerField(null=True)
    email = models.EmailField(max_length=250,null=True)
    photo = models.ImageField(upload_to="img",null=True)
    #batchhandling = models.ForeignKey("batch",on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.id)
    

class batch(models.Model):
    Teacher = models.ForeignKey("teacher",on_delete=models.CASCADE)
    Student = models.ForeignKey("student",on_delete=models.SET_NULL,null=True) #since there can be many other students in the batch 
    totalclasses = models.IntegerField()
    completedclasses = models.IntegerField()
    def __str__(self):
        return str(self.id)