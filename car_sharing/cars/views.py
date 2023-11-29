from django.shortcuts import render
# Create your views here.

def home(request):
    
    return render(request, "cars/base.html")


def index(request):
    return render(request, 'cars/index.html')
