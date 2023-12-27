from django.shortcuts import HttpResponse, render


# Create your views here.
def home():
    return HttpResponse("<h5>Home</h5>")
