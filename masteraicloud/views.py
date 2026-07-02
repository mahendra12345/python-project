from django.http import HttpResponse
from . import views
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello how are you")
    return render(request,'website/home.html')

def about(request):
    # return HttpResponse("Tell me something abou yourself")
    return render(request,'website/about.html')