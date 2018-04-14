from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.

#create views for our REST api

#from rest_framework import status
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
=======
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
>>>>>>> 119d5089c749b5d9ed8d3650fd2e9f93751fdb1b
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers
from rest_framework import generics
from snippets.serializers import UserSerializer
from rest_framework import permissions

from django.contrib.auth.models import User
from snippets.permissions import IsOwnerOrReadOnly

<<<<<<< HEAD
"""
#views of our API's
@api_view(['GET', 'POST'])
def snippet_list(request):
	#list of all code snipptes, or create  a new snippet
	if request.method == 'GET
=======

#views of our API's

class SnippetList(APIView):
	def get(self, request, format = None):

>>>>>>> 119d5089c749b5d9ed8d3650fd2e9f93751fdb1b
		snippets = Snippet.objects.all()
		serializer = SnippetSerializers(snippets, many = True)
		return Response(serializer.data)

	def post(self, request, format = None):

		
		serializer = SnippetSerializers(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#View of retrieve update and delete snippet request


# Updae delete


<<<<<<< HEAD

class SnippetDetail(APIView):
	def get_object(self, pk):
=======
#Helo
>>>>>>> 966af99518d707fecd3fcbdddaddcc1428d22a13

	#Retrieve update or delete a code snippet
		try:
			snippet = Snippet.objects.get(pk = pk)
		except Snippet.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		snippet = self.get_object(pk)

		serializer = SnippetSerializers(snippet)
		return Response(serializer.data)

	def put(self, request, pk, format = None):
		snippet = self.get_object(pk)
		
		serializer = SnippetSerializers(snippet, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	def delete(self, request, pk, format = None):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response(status= status.HTTP_204_NO_CONTENT)

"""


# GENERIC VIEWS


# REST framework provides a set of already mixed-in generic views that we can use to trim down our views.py module even more.


class SnippetList(generics.ListCreateAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializers
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

	def perform_create(self , serializer):
		serializer.save(owner = self.request.user)

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializers


# We'll also add a couple of views to views.py. We'd like to just use read-only views for the user representations, so we'll use the ListAPIView and RetrieveAPIView generic class-based views.

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

