from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def about(request):
    return HttpResponse('<h1><marquee>Hello... My name is Venu Gopal, I am From Chilakaluripet')