from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework import serializers

from .models import Snippet
from .serializers import SnippetSerializer


def home():
    return HttpResponse("<h5>Home</h5>")

# Similar to @app.route("/", methods=[] from flask.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
