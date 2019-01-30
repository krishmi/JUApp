from django.urls import path
from . import views

urlpatterns=[
	path('logout/',views.logout,name='logout'),
	path('<placeholder>/',views.index,name='index'),
	path('<placeholder>/create/',views.add,name='add'),
	path('<placeholder>/verify/',views.verify,name='verify'),
	path('<placeholder>/<dept>/',views.subject,name='subject'),
	path('<placeholder>/<dept>/<subject>/',views.resource,name='resource'),
	path('<placeholder>/<dept>/<subject>/<resource>/',views.uploading,name='upload'),
	path('<placeholder>/<dept>/<subject>/<resource>/<res_name>',views.pdf_response,name='pdf'),
#	path('<dept>/<subject>/',views.subject,name='subject'),
#	path('<dept>/<subject>/<resource>/login/',views.login,name='login'),
#	path('<dept>/<subject>/<resource>/login/create/',views.create,name='create'),
#	path('<dept>/<subject>/<resource>/login/create/add/',views.add,name='add'),
#	path('<dept>/<subject>/<resource>/login/verify/',views.verify,name='verify'),
#	path('<dept>/<subject>/<resource>/<resource_name>/',views.pdf_response,name='pdf_response'),
#	path('<dept>/<subject>/<resource>/login/verify/uploadFile/',views.uploading,name='upload'),
]