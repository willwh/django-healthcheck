from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import BadRequest

# Create your views here.

def index(request):
    # connect and test the things
    
    # if failed, puke
    if (foo):
        raise BadRequest('Invalid request.')
    else:
        return HttpResponse("Things are okay.")