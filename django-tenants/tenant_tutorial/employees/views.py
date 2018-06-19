from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from employees.models import  Employees
from employees.serializers import EmployeeSerializer
from rest_framework import status
#from tenant_schemas.utils import get_tenant_model, remove_www_and_dev, get_public_schema_name
#from customers.models import Client
#from django.db import connection
import pdb


# Create your views here.

class EmployeeDetails(APIView):

	def get(self,request,format=None):
		employees=Employees.objects.all()
		#pdb.set_trace()
		serializer=EmployeeSerializer(employees,many=True)
		return Response(serializer.data)
