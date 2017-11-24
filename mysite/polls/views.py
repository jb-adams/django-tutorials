from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """index page view for polls app"""
    return HttpResponse("Hello, world. You're at the polls index.")
