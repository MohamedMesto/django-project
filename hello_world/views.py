from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


""" def index(index):
    return HttpResponse("Salam, world!")
"""
""" 
def index(request):

   if request.method == "GET":
       return HttpResponse("This was a GET request")
   elif request.method == "POST":
       return HttpResponse("This was a POST request") 
"""

def index(request):

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)