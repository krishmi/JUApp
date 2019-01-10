from django.db import models

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