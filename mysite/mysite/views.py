#I have created this file-Jaydeep

from django.http import HttpResponse

def index(request):
    return HttpResponse("""<a href="https://web.whatsapp.com/"> Click Here to open Wattsapp web</a>""")

def about(request):
    return HttpResponse("<h1>Hii its me Jaydeep</h1>")

def removepunc(request):
    return HttpResponse("Removepunc")

def capfirst(request):
    return HttpResponse("Capitalize First")


def newlineremove(request):
    return HttpResponse("New line Remove")

def spaceremove(request):
    return HttpResponse("Space remove")

def charcount(request):
    return HttpResponse("Char Count")