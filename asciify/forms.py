from django import forms
from .models import Upload, Hotel

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['image', 'action']
        
class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] 