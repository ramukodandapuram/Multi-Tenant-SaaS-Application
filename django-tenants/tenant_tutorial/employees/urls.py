from django.conf.urls import url
from . import views

urlpatterns =[

			url(r'^employees/$',views.EmployeeDetails.as_view()),


]