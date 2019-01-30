from django.db import models
import os
# Create your models here.
class Subjects(models.Model):
	semesters=(
			('First','First'),
			('Second','Second'),
			('Third','Third'),
			('Fourth','Fourth'),
			('Fifth','Fifth'),
			('Sixth','Sixth'),
			('Seventh','Seventh'),
			('Eighth','Eighth'),
		
		  )
	dept_choice=(
				('Information Technology','Information Technology'),
				('Construction','Construction'),
				('Power','Power'),
				('Printing','Printing'),
				('Instrumentation','Instrumentation'),
				)
	name=models.CharField(max_length=50)
	dept=models.CharField(max_length=50,choices=dept_choice)
	sem=models.CharField(max_length=10,choices=semesters,default='First')

def getPath(instance,filename):
	var= os.path.join(instance.app,instance.subject,instance.resource,filename)
	return var
	
class Upload(models.Model):
	app='media/'
	subject=models.CharField(max_length=100, default='')
	resource=models.CharField(max_length=100,default='')
	file=models.FileField(upload_to=getPath)

class User(models.Model):
	dept_choice=(
				('Information Technology','Information Technology'),
				('Construction','Construction'),
				('Power','Power'),
				('Printing','Printing'),
				('Instrumentation','Instrumentation'),
				)
	name=models.CharField(max_length=100,default='')
	uname=models.CharField(max_length=100,default='')
	password=models.CharField(max_length=20,default='')
	dept=models.CharField(max_length=50,choices=dept_choice)
	roll=models.CharField(max_length=20)
	key=models.CharField(max_length=100,default='')