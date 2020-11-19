from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def func2 (request):
    return HttpResponse ('func2 view')
