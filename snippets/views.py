from django.shortcuts import HttpResponse, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_exempt
from rest_framework import serializers
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer


def home():
    return HttpResponse("<h5>Home</h5>")


@csrf_exempt
def snippet_list(request):
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update, or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)  # Update `snippet` with data

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

        return HttpResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(status=204)
