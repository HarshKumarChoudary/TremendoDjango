from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
import uuid
from .forms import teacherprofileform, studentprofileform,simgform,timgform
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return redirect('login_attempt')

@login_required
def simg(request):
    if request.method == 'POST':
        form = simgform(request.POST,request.FILES)
        if form.is_valid():
            if student.objects.filter(profile=profile.objects.get(user = request.user)).exists():
                std=student.objects.get(profile=profile.objects.get(user = request.user))
                std.photo=form.cleaned_data['photo']
                std.save()
    return redirect('student_dashboard')

@login_required 
def timg(request):
    if request.method == 'POST':
        form = timgform(request.POST,request.FILES)
        if form.is_valid():
            if teacher.objects.filter(profile=profile.objects.get(user = request.user)).exists():
                std=teacher.objects.get(profile=profile.objects.get(user = request.user))
                std.photo=form.cleaned_data['photo']
                std.save()
    return redirect('teacher_dashboard')


class student_dashboard(View):
    def get(self,request):
        form=studentprofileform()
        imgform = simgform()
        if student.objects.filter(profile=profile.objects.get(user = request.user)).exists():
            im = student.objects.get(profile=profile.objects.get(user = request.user))
        return render(request,'sdash.html',{'form':form,'active':'btn-primary','imgform':imgform,'im':im})

    def post(self,request):
        form = studentprofileform(request.POST,request.FILES)
        if form.is_valid():
            if student.objects.filter(profile=profile.objects.get(user = request.user)).exists():
                std=student.objects.get(profile=profile.objects.get(user = request.user))
                std.name=form.cleaned_data['name']
                std.gender=form.cleaned_data['gender']
                std.email=form.cleaned_data['email']
                std.address=form.cleaned_data['address']
                std.save()
            else:
                return redirect('error')
            messages.success(request,'Congratulation! Profile Updated Successfully')
        form1 = studentprofileform()
        imgform = simgform()
        if student.objects.filter(profile=profile.objects.get(user = request.user)).exists():
            im = student.objects.get(profile=profile.objects.get(user = request.user))
    
        return render(request,'sdash.html',{'form':form1,'active':'btn-primary','imgform':imgform,'im':im}) 
   

class teacher_dashboard(View):
    def get(self,request):
        form=teacherprofileform()
        imgform = timgform()
        if teacher.objects.filter(profile=profile.objects.get(user = request.user)).exists():
            im = teacher.objects.get(profile=profile.objects.get(user = request.user))
        return render(request,'tdash.html',{'form':form,'active':'btn-primary','imgform':imgform,'im':im})

    def post(self,request):
        form = teacherprofileform(request.POST,request.FILES)
        if form.is_valid():
            if teacher.objects.filter(profile=profile.objects.get(user = request.user)).exists():
                std=teacher.objects.get(profile=profile.objects.get(user = request.user))
                std.name=form.cleaned_data['name']
                std.phone_no=form.cleaned_data['phone_no']
                std.email=form.cleaned_data['email']
                std.address=form.cleaned_data['address']
                std.save()
            else:
                return redirect('error')
            messages.success(request,'Congratulation! Profile Updated Successfully')
        form1 = teacherprofileform()
        imgform = timgform()
        if teacher.objects.filter(profile=profile.objects.get(user = request.user)).exists():
            im = teacher.objects.get(profile=profile.objects.get(user = request.user))
    
        return render(request,'tdash.html',{'form':form1,'active':'btn-primary','imgform':imgform,'im':im}) 
   


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if profile.objects.get(user = user).is_verified:
                    login(request , user)
                    if teacher.objects.filter(profile=profile.objects.get(user = user)).exists():
                        messages.success(request, 'teacher found.')
                        return redirect('teacher_dashboard')
                    else:
                        messages.success(request, 'student found.')
                        return redirect('student_dashboard')
                else:
                    messages.success(request, 'Profile is not verified check your mail.')
                    return redirect('/login')
        else:
            messages.success(request, 'Wrong password or username')
            return redirect('/login')

    return render(request,'login.html')


    
    

def success(request):
    return render(request,'success.html')

def token_send(request):
    return render(request, 'token_send.html')


def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        typ = request.POST.get('type')
        password = request.POST.get('password')
        if User.objects.filter(username=username).first():
            messages.success(request, 'Username is taken.')
            return redirect('/register')
        if User.objects.filter(email=email).first():
            messages.success(request, 'Email is taken.')
            return redirect('/register')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        profileobj = profile.objects.create(user = user_obj, auth_token=auth_token)
        profileobj.save()
        if typ == "teacher":
            teach = teacher.objects.create(profile=profileobj)
            teach.save()
        else:
            stud = student.objects.create(profile=profileobj)
            stud.save()

        send_mail_after_registration(email, auth_token)
        return redirect('/token')

    return render(request,'register.html')

def error_page(request):
    return  render(request , 'error.html')

def verify(request , auth_token):
    try:
        profile_obj = profile.objects.filter(auth_token = auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')
    
def send_mail_after_registration(email, token):
    subject = "Your's account needs to be verified"
    message = f'Hi, Please verify your account here https://127.0.0.1:8000/verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
