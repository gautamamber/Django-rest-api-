from rest_framework import serializers
from . models import Employees
class employeeSerializer(serializers.ModelSerializer):
	class Meta:
		model  = Employees
		fields = ('firstname' , 'lastname', 'emp_id')
