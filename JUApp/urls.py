from django.urls import path
from . import views

urlpatterns=[
	path('<dept>/',views.index,name='index'),
	path('<dept>/<subject>/',views.subject,name='subject'),
	path('<dept>/<subject>/<resource>/login/',views.login,name='login'),
	path('<dept>/<subject>/<resource>/<resource_name>/',views.pdf_response,name='pdf_response'),
	path('<dept>/<subject>/<resource>/login/uploadFile/',views.uploading,name='upload'),
	path('<dept>/<subject>/<resource>/login/uploadFile/create',views.create,name='create'),
	path('<dept>/<subject>/<resource>/login/uploadFile/verify',views.verify,name='verify'),
]