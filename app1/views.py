from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def func1 (request):
    return HttpResponse ('func1 view')
