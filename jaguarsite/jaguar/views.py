from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import tools


def index(request):
    return HttpResponse(" Nothing to do here ")


def ReloadArchives(request):
    tools.register_Archives()
    return HttpResponse(" Reload ....  Done <BR>  <a href='/jaguar/admin'> Back to Jaguar</a> ")
