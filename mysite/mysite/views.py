#I have created this file-Jaydeep

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello")