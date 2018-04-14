from django.shortcuts import render

# Create your views here.

#create views for our REST api

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers


#views of our API's
@api_view(['GET', 'POST'])
def snippet_list(request):
	#list of all code snipptes, or create  a new snippet
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializers(snippets, many = True)
		return Response(serializer.data)

	elif request.method == 'POST':
		
		serializer = SnippetSerializers(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#View of retrieve update and delete snippet request


# Updae delete



@api_view(['GET', 'PUT', 'DELETE'])
def snippet_details(request, pk):
	#Retrieve update or delete a code snippet
	try:
		snippet = Snippet.objects.get(pk = pk)
	except Snippet.DoesNotExist:
		return Response(status = status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = SnippetSerializers(snippet)
		return Response(serializer.data)

	elif request.method == 'PUT':
		
		serializer = SnippetSerializers(snippet, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	elif request.method  == 'DELETE':
		snippet.delete()
		return Response(status= status.HTTP_204_NO_CONTENT)

