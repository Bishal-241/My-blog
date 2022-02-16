# from django.http import HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is my home page")
    return render(request,'index.html')
def service(request):
    return HttpResponse("This is my services page")

def contact(request):
    return HttpResponse("This is my contact page")

def project(request):
    return HttpResponse("This is my project page")

def about(request):
    return HttpResponse("This is my login page")