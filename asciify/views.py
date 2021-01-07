from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'asciify/home.html')

def about(request):
    return HttpResponse('<h1>FilterMe About</h1>')
