from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    
    # This simple shortcut replaces all previous code, definitions and functions
    class Meta:
        model = Snippet
        # On serializers, as opposed to Django Models, the '__all__' string doesn't indicate to use all fields
        # it only requires to specifie the model deinition (model = Snippet) to serialize all fields,
        # only use fields attribute whenever specific attributes are going to be serialized.
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style') 
