from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from .models import *

class teacherprofileform(forms.ModelForm):
    class Meta:
        model = teacher
        fields=['name','address','email','phone_no']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'address':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'phone_no':forms.NumberInput(attrs={'class':'form-control'})}
        
class studentprofileform(forms.ModelForm):
    class Meta:
        model = student
        fields=['name','gender','email','address']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'gender':forms.Select(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'}),'address':forms.TextInput(attrs={'class':'form-control'})}

class simgform(forms.ModelForm):
    class Meta:
        model = student
        fields = ['photo']
        labels = {'Image':''}

class timgform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['photo']
        labels = {'Image':''}

class loginform(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password= forms.CharField(label= _("Password"),strip=False,widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control','autocomplete':'current-password'}))

class passwordchangeform(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

class passwordresetform(PasswordResetForm):
    email = forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))

class setpasswordform(SetPasswordForm):
    new_password1=forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
