from django import forms
from .models import Transport_Mem
import re

class CustomTransport(forms.ModelForm):
  class Meta:
    model=Transport_Mem
    fields=['name','email','phone_number','profile','Age','Address']
    widgets={
      'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Driver Name'}),
      'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
      'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter 10 digit number'}),
      'Age':forms.DateInput(attrs={'class':'form-control','type':'date'}),
      'Address':forms.Textarea(attrs={'class':'form-control','rows':2,'placeholder':'Your Address Enter'})
    }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise forms.ValidationError("Enter a valid email address.")
        return email

    def clean_phone_number(self):
        mobile = self.cleaned_data.get('mobile_number')
        if not mobile:
            raise forms.ValidationError("Mobile number is required.")
        if not re.match(r'^[6-9]\d{9}$', mobile):
            raise forms.ValidationError("Enter a valid 10-digit Indian mobile number starting with 6, 7, 8, or 9.")
        return mobile
    
    