from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.Serializer):
    
    # This simple shortcut replaces all previous code, definitions and functions
    class Meta:
        model = Snippet
        fields = [ '__all__' ]
