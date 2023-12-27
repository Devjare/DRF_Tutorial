from django.http import Http404

from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer


def home():
    return HttpResponse("<h5>Home</h5>")

# Similar to @app.route("/", methods=[] from flask.
class SnippetList(APIView):
    def get(request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrieve, update, or delete a code snippet.
    """

    def get_snippet(self, pk):
        try:
            snippet = Snippet.objects.get(pk=pk)
            return snippet
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_snippet(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        snippet = self.get_snippet(pk)
        serializer = SnippetSerializer(snippet, data=request.data)  # Update `snippet` with data

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_snippet(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
