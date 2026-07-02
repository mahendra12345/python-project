from django.shortcuts import render

# Create your views here.
def all_master(request):
    return render(request,'master/all_master.html')