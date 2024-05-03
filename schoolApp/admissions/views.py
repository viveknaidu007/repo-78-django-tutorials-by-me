from django.shortcuts import render
from django.http import HttpResponse #http response we have to import first, 
# Create your views here.

#function based views , class based views

def addAdmission(request):
    return HttpResponse("<h1> this is add admission view </h1> <h2> welcome to my school app </h2>")


def admissionsreport(request):
    return HttpResponse("this is admisiion report view")
