from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from django import forms
from .models import *



class StudentForm(ModelForm):

	class Meta():
		model = Student
		fields = '__all__'
		
		
class ProjectForm(ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		


# customise user creation form
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']