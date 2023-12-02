from django.http import HttpResponse
from django.shortcuts import render

# create your views here.
def demo(request):

     return render(request,"index.html")

#def addition (request):
     #return render(request,"about.html")



