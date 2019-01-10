from django.urls import path
from . import views

urlpatterns=[
	path('<dept>/',views.index,name='index')
]