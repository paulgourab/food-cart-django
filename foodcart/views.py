from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    """return http response"""
    # return HttpResponse("Hello, World!")
    """return template"""
    return render(request, 'test.html')