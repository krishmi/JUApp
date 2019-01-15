from django.urls import path
from . import views

urlpatterns=[
	path('<dept>/',views.index,name='index'),
	path('<dept>/<subject>/',views.subject,name='subject'),
	path('<dept>/<subject>/<resource>/login/',views.login,name='login'),
	path('<dept>/<subject>/<resource>/login/create/',views.create,name='create'),
	path('<dept>/<subject>/<resource>/login/verify/',views.verify,name='verify'),
	path('<dept>/<subject>/<resource>/<resource_name>/',views.pdf_response,name='pdf_response'),
	path('<dept>/<subject>/<resource>/login/verify/uploadFile/',views.uploading,name='upload'),
]