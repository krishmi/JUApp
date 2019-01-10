from django.shortcuts import render
from .models import Subjects

# Create your views here.

def index(request,dept):
	if dept=='index':
		return render(request,'index.html',{'flag':False})
	else:
		s1=Subjects.objects.filter(dept=dept,sem='First')
		print(s1.count())
		s2=Subjects.objects.filter(dept=dept,sem='Second')
		print(s2.count())
		s3=Subjects.objects.filter(dept=dept,sem='Third')
		s4=Subjects.objects.filter(dept=dept,sem='Fourth')
		s5=Subjects.objects.filter(dept=dept,sem='Fifth')
		s6=Subjects.objects.filter(dept=dept,sem='Sixth')
		s7=Subjects.objects.filter(dept=dept,sem='Seventh')
		s8=Subjects.objects.filter(dept=dept,sem='Eighth')
		return render(request,'index.html',{'flag':True,'s1':s1,'s2':s2,'s3':s3,'s4':s4,'s5':s5,'s6':s6,'s7':s7,'s8':s8})