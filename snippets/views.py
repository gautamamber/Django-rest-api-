from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializers



#views of our API's

class SnippetList(APIView):
	def get(self, request, format = None):

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

