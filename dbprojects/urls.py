from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),  
	path('', views.homePage, name="home"),
	path('home_main/', views.homePageMain, name="home_main"),
	path('creates/', views.createStudent, name="creates"),
	path('createp/', views.createProject, name="createp"),

	path('read/', views.viewPage, name="read"),
	path('viewupdate/<str:pk1>/<str:pk2>', views.viewupdatePage, name="viewupdate"),
	path('viewdelete/<str:pk>', views.viewdeletePage, name="viewdelete"),

	path('supdate/', views.updatesPage, name="supdate"),
	path('pupdate/', views.updatepPage, name="pupdate"),
	path('updates/<str:pk>/', views.updateStudent, name="updates"),
	path('updatep/<str:pk>/', views.updateProject, name="updatep"),

	path('sdelete/', views.deletesPage, name="sdelete"),
	path('pdelete/', views.deletepPage, name="pdelete"),
	path('deletes/<str:pk>/', views.deleteStudent, name="deletes"),
	path('deletep/<str:pk>/', views.deleteProject, name="deletep"),

	# path('delete/', views.deletePage, name="delete"),
	

]