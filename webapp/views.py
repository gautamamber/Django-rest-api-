from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Employees
from . serializers import employeeSerializer
from rest_framework import status

class employeeList(APIView):


	# Reading data			
	def get(self, request):
		employees1 = Employees.objects.all()
		serializer = employeeSerializer(employees1, many = True)
		return Response(serializer.data)

		#Write mode
	def post(self):
		pass