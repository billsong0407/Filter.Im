from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm, HotelForm
from .models import Hotel, Upload

def home(request):
    if request.method == 'POST': 
        form = UploadForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('about')
    else: 
        form = UploadForm()  
    return render(request, 'asciify/home.html', {'form': form})

def about(request):
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        image = Upload.objects.all()  
        return render(request, 'asciify/about.html', 
                     {'upload' : image[0]})
