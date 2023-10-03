from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest,HttpResponse


def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request, 'blog.html')

def features(request):
    return render(request, 'features.html')

def contact(request):
    return render(request, 'contact.html')
def login(request):
    return render(request, 'login.html')