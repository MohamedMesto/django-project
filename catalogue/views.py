from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.




def catalogue(request):
    return HttpResponse("Home Electronic, Other Accessories")