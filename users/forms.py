from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
	username=forms.CharField(required=True,label='Username',max_length=100,
		widget=forms.TextInput(attrs={'class':'input','placeholder':'username'}))
	email=forms.CharField(required=False,label='Email',
		widget=forms.EmailInput(attrs={'class':'email'}))
	password1=forms.CharField(required=True,label='password',
		widget=forms.PasswordInput(attrs={'class':'pass'}))
	password2=forms.CharField(required=True,label='password',
		widget=forms.PasswordInput(attrs={'class':'pass'}))
	class Meta:
		model=User
		fields=('username','email','password1','password2')