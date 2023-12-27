from django.contrib.auth.models import User

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework import serializers

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


def home():
    return HttpResponse("<h5>Home</h5>")

# Similar to @app.route("/", methods=[] from flask.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [ permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly ]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

