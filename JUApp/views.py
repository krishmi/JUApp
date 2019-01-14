from django.shortcuts import render
from .models import Subjects
from .forms import UploadForm
from .models import Upload
from django.http import HttpResponse,HttpResponseRedirect
import os

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

def subject(request,dept,subject):
	books=os.listdir('/home/krishna/JUApp/media/'+subject+'/'+'book/')
	slides=os.listdir('/home/krishna/JUApp/media/'+subject+'/slide/')
	notes=os.listdir('/home/krishna/JUApp/media/'+subject+'/note/')
	questions=os.listdir('/home/krishna/JUApp/media/'+subject+'/question/')
	return render(request,'subject.html',{'subject':subject,'books':books,'slides':slides,'notes':notes
		,'questions':questions})

def pdf_response(request,subject,dept,resource,resource_name):
	with open('/home/krishna/JUApp/media/'+subject+'/'+resource+'/'+resource_name, 'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline'
		return response
	pdf.closed

def login(request,dept,subject,resource):
	form=UploadForm()
	return render(request,'login.html',{'sub':subject,'res':resource,'form':form})

def uploading(request,subject,dept,resource):
	inst=Upload()
	inst.subject=subject
	inst.resource=resource
	inst.save();
	upload=UploadForm(request.POST,request.FILES,instance=inst)
	if upload.is_valid():
		upload.save(commit=True)
		return HttpResponseRedirect('/JUApp/'+dept+'/'+subject+'/')
	else:
		return HttpResponseRedirect('/JUApp/')
	
