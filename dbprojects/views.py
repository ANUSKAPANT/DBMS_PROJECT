from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import *
from .models import *
from .filters import *
from .decorators import *

# Create your views here.

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)  #can also use UserCreationForm
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')		
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}
	return render(request, 'template/register.html', context)


@unauthenticated_user
def loginPage(request):
	
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'template/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def homePage(request):
	return render(request, 'template/home.html', {})

@login_required(login_url='login')
def homePageMain(request):
	return render(request, 'template/homepage.html', {})

@login_required(login_url='login')
def createProject(request):
	formp = ProjectForm()
	if request.method == 'POST':
		formp = ProjectForm(request.POST)
		if formp.is_valid():
			formp.save()
			return redirect('/home_main')
	context = {'formp':formp}
	return render(request, 'template/create_project.html', context)

@login_required(login_url='login')
def createStudent(request):

	forms = StudentForm()
	
	if request.method == 'POST':
		
		forms = StudentForm(request.POST)

		if forms.is_valid():
			forms.save()
			return redirect('/home_main')
		
	context = {'forms':forms}
	return render(request, 'template/create_student.html', context)


@login_required(login_url='login')
def viewPage(request):
	projects = Project.objects.all()
	students = Student.objects.select_related()
	a = StudentFilter(request.GET, queryset=students)  
	b = ProjectFilter(request.GET, queryset=projects)
	mylist = zip(students,projects)
	students = a.qs
	projects = b.qs 
	context = {'a':a, 'b':b, 'mylist':mylist, 'students':students, 'projects':projects}
	return render(request, 'template/read.html', context)

@login_required(login_url='login')
def viewupdatePage(request, pk1, pk2):

	student = Student.objects.get(id=pk1)
	project = Project.objects.get(id=pk2)
	form1 = StudentForm(instance=student)
	form2 = ProjectForm(instance=project)
	
	if request.method == 'POST':
		form1 = StudentForm(request.POST, instance=student)
		form2 =ProjectForm(request.POST, instance=project)
		if form1.is_valid() and form2.is_valid():
			form1.save()
			form2.save()
			return redirect('/read')
		
	context = {'form1':form1, 'form2': form2 }
	return render(request, 'template/view_update.html', context)





@login_required(login_url='login')
def viewdeletePage(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == "POST":
		student.delete()
		return redirect('/read')
	context = {'item':student}
	return render(request, 'template/view_delete.html', context)


@login_required(login_url='login')
def updatesPage(request):
	# projects = Project.objects.all()
	students = Student.objects.all()
	myFilter = StudentFilter(request.GET, queryset=students)  
	students = myFilter.qs
	context = {'students':students, 'myFilter':myFilter}  
	return render(request, 'template/updates.html', context)

@login_required(login_url='login')
def updatepPage(request):
	projects = Project.objects.all()
	myFilter = ProjectFilter(request.GET, queryset=projects)
	projects = myFilter.qs 
	context = {'myFilter': myFilter,'projects':projects}    
	return render(request, 'template/updatep.html', context)

@login_required(login_url='login')
def updateStudent(request, pk):
	student = Student.objects.get(id=pk)
	form = StudentForm(instance=student)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('/supdate')
	context = {'form':form }
	return render(request, 'template/update_student.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
	project = Project.objects.get(id=pk)
	form = ProjectForm(instance=project)
	
	if request.method == 'POST':
		form =ProjectForm(request.POST, instance=project)
		if form.is_valid():
			form.save()
			return redirect('/pupdate')
	context = {'form':form}
	return render(request, 'template/update_project.html', context)

@login_required(login_url='login')
def deletesPage(request):
	students = Student.objects.all()
	a = StudentFilter(request.GET, queryset=students)  
	students = a.qs	
	context = {'students':students, 'a':a}    
	return render(request, 'template/deletes.html', context)

@login_required(login_url='login')
def deletepPage(request):
	projects = Project.objects.select_related()
	b = ProjectFilter(request.GET, queryset=projects)
	projects = b.qs 
	context = {'projects':projects, 'b':b}    
	return render(request, 'template/deletep.html', context)

@login_required(login_url='login')
def deleteStudent(request, pk):
	student = Student.objects.get(id=pk)
	if request.method == "POST":
		student.delete()
		return redirect('/sdelete')
	context = {'item':student}
	return render(request, 'template/delete_student.html', context)

@login_required(login_url='login')
def deleteProject(request, pk):
	project = Project.objects.get(id=pk)
	if request.method == "POST":
		project.delete()
		return redirect('/pdelete')
	context = {'item':project}	
	return render(request, 'template/delete_project.html', context)




