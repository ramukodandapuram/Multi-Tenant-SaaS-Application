from employees.models import Employees
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employees
		fields=('name','surnames','email','phone_number')
