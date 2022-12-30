from django.shortcuts import render
from django.http import HttpResponse
# Create your view
# s here.


def firstview(request):
    return HttpResponse('I am groot')