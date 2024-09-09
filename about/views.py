from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def about_me(request):
    return HttpResponse("About Me I completed my bachelors degree in the College of Electronic Engineering at the University of Aleppo in the field of computer engineering, then I held several jobs, the last of which was: I worked for a few years as an employee and lecturer in a number of colleges affiliated with the University of Aleppo, such as the College of Education and Science and the Computer Institute, as well as at Al-Mamoun Private University. As God Almighty commanded us to be positive on earth and help our brothers and sisters from the children of Adam and Eve, peace be upon them! Berlin - Mohamed Mesto")