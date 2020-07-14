import django_filters 
from .models import *

class StudentFilter(django_filters.FilterSet):
	
	class Meta:
		model = Student
		fields = '__all__'	
				

class ProjectFilter(django_filters.FilterSet):
	
	class Meta:
		model = Project
		fields = '__all__'
		exclude = ['title']	
		