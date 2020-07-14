from django.db import models

# Create your models here.

class Project(models.Model):

	title = models.CharField(max_length = 200, null = True, unique = True) 
	category = models.CharField(max_length = 200, null = True)
	choice = (
				('Anand Kumar Shah','Anand Kumar Shah'),
				('Basanta Joshi','Basanta Joshi'),
				('Daya Sagar Baral','Daya Sagar Baral'),
				('Dibakar Pant','Dibakar Pant'),
				('Dinesh Kumar Sharma','Dinesh Kumar Sharma'),
				('Jitendra Kumar Manadhar','Jitendra Kumar Manadhar'),
				('Nanda Bikram Adhikari','Nanda Bikram Adhikari'),
				('Ram Krishna Maharjan','Ram Krishna Maharjan'),
				('Ranju Kumar Shiwakoti','Ranju Kumar Shiwakoti'),
				('Sanjeeb Prasad Panday','Sanjeeb Prasad Panday'),
				('Subarna Shakya','Subarna Shakya'),
				('Surendra Shrestha','Surendra Shrestha')
			)
	supervisor = models.CharField(max_length = 200, null = True, choices = choice)

	
	class Meta:
		unique_together = ["title", "category", "supervisor"]

	def __str__(self):
		return self.title


class Student(models.Model):
	choice = (('BEX','BEX'),('BEX','BCT'))
	name = models.CharField(max_length = 200, null = True)
	batch = models.CharField(max_length = 200, null = True)
	program = models.CharField(max_length = 200, null = True, choices = choice)
	roll_number = models.CharField(max_length = 200, null = True)
	project = models.ForeignKey(Project, blank = True, null = True, on_delete = models.SET_NULL)

	
	class Meta:
		unique_together = ["name", "project"]

	def __str__(self):
		return self.name 






