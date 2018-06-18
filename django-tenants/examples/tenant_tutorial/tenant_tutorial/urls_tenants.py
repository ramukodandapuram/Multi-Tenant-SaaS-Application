from customers.views import TenantView
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
#from employees.views import EmployeeDetails


urlpatterns = [
    path('', TenantView.as_view()),
    #path('admin/', admin.site.urls),
    url(r'^',include('employees.urls')),
    url(r'^admin/',admin.site.urls),


    ]
