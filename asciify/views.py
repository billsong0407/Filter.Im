from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm, HotelForm
from .models import Hotel, Upload

def home(request):
    if request.method == 'POST': 
        form = UploadForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('result')
    else: 
        form = UploadForm()  
    return render(request, 'asciify/home.html', {'form': form})

def result(request):
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        image = Upload.objects.latest('created')
        # entries= Upload.objects.all()
        # entries.delete()
        return render(request, 'asciify/result.html', 
                     {'upload' : image})
