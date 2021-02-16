from django.http import HttpResponse as HR
from django.shortcuts import render

def home(request):
    return HR('Welcome home mf')

def about(request):
    return HR('ur mum')