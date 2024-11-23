from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'main/index.html')

def ciolk(request):
    return render(request,'main/ciolk.html')

def perelman(request):
    return render(request,'main/perelman.html')

def kapica(request):
    return render(request,'main/kapica.html')

